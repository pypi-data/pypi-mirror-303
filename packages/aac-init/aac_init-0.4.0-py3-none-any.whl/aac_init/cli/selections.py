# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Rudy Lei <shlei@cisco.com>

import os
import traceback

from typing import Any, Dict, Optional
from aac_init.log_utils import setup_logger
from aac_init.conf import settings
from ruamel import yaml
from aac_init.tools import (
    YamlTool,
    ThreadTool,
    ApicCimcTool,
    AciSwitchTool,
    ApicTool,
    AnsibleTool,
)


class Selections:
    """
    Handle CLI selections
    """

    def __init__(self, data_path: str, output_path: str):
        self.logger = setup_logger("selections.log")

        self.logger.debug(
            f"Loaded selections with data_path: '{data_path}', "
            f"output_path: '{output_path}'"
        )

        self.data: Optional[Dict[str, Any]] = None
        self.data_path = data_path
        self.output_path = output_path
        self.fabric_mgmt = None
        self.global_policy = None

        self.yaml_tool = YamlTool(self.data_path, self.output_path)
        self._load_global_policy()

        if not self.global_policy:
            self.logger.error("Failed to load global policy!")
            exit(1)

        self.logger.debug("Selections initialized successfully!")

    def _load_global_policy(self):
        """Load global policy"""

        self.logger.debug("Loading global policy...")
        for dir, _, files in os.walk(self.data_path):
            for filename in files:
                if filename in settings.DEFAULT_DATA_PATH:
                    self.global_policy_path = os.path.join(dir, filename)
        if self.global_policy_path:
            self.global_policy = self.yaml_tool.load_yaml_file(self.global_policy_path)
            self.logger.debug("'00-global_policy' loaded successfully.")
            return True
        else:
            self.logger.error("'00-global_policy' is missing!")
            return False

    def _load_fabric_mgmt(self):
        """Load fabric mgmt"""

        self.logger.debug("Loading fabric mgmt...")
        for dir, _, files in os.walk(self.data_path):
            for filename in files:
                if filename in settings.DEFAULT_FABRIC_MGMT_PATH:
                    self.fabric_mgmt_path = os.path.join(dir, filename)
        if self.fabric_mgmt_path:
            self.fabric_mgmt = self.yaml_tool.load_yaml_file(self.fabric_mgmt_path)
            if not self.fabric_mgmt:
                self.logger.error("Failed to load fabric mgmt!")
                return False
            self.logger.debug("'01-fabric-mgmt' loaded successfully.")
            return True
        else:
            self.logger.error("'01-fabric-mgmt' is missing!")
            return False

    def fabric_bootstrap(self):
        """
        Method: 01-fabric_bootstrap
        Description: Wipe and boot APIC/switch to particular version
        """

        self.logger.info("Start to bootstrap ACI fabric...")

        fabric_policy = self.global_policy.get("fabric", {})
        global_policies = fabric_policy.get("global_policies", {}) or {}
        apic_check = "apic_nodes_connection" in fabric_policy
        aci_switch_check = "switch_nodes_connection" in fabric_policy

        fabric_bootstrap_threads = []

        # Validate APICs if have
        if apic_check:
            apics = fabric_policy.get("apic_nodes_connection", []) or []

            for apic_cimc_connection in apics:
                apic = ApicCimcTool(global_policies, apic_cimc_connection, apics)
                if not apic.api_validate_apic():
                    self.logger.error(f"Validate APIC '{apic.hostname}' failed!")
                    return False
                self.logger.info(f"Validate APIC '{apic.hostname}' successfully.")
                thread = ThreadTool(target=apic.gen_install_apic)
                fabric_bootstrap_threads.append((apic.hostname, thread))
                self.logger.debug(f"Add APIC '{apic.hostname}' to thread successfully.")

        # Validate ACI switches if have
        if aci_switch_check:
            aci_switches = fabric_policy.get("switch_nodes_connection", []) or []

            # Load fabric mgmt
            if self._load_fabric_mgmt():
                fabric_mgmt_policy_apic = self.fabric_mgmt.get("apic", {}) or {}
                fabric_mgmt_policy_apic_node_policies = (
                    fabric_mgmt_policy_apic.get("node_policies", {}) or {}
                )
                aci_switches_mgmt = (
                    fabric_mgmt_policy_apic_node_policies.get("nodes", []) or []
                )
            else:
                self.logger.error("Unable to load fabric mgmt info!")
                return False

            for aci_switch_connection in aci_switches:
                aci_switch_mgmt = next(
                    (
                        node
                        for node in aci_switches_mgmt
                        if node["id"] == aci_switch_connection["id"]
                    ),
                    {},
                )

                aci_switch = AciSwitchTool(
                    global_policies, aci_switch_connection, aci_switch_mgmt
                )
                if not aci_switch.validate_aci_switch():
                    self.logger.error(
                        f"Validate ACI switch '{aci_switch.hostname}' failed!"
                    )
                    return False
                self.logger.info(
                    f"Validate ACI switch '{aci_switch.hostname}' successfully."
                )
                thread = ThreadTool(target=aci_switch.install_aci_switch)
                fabric_bootstrap_threads.append((aci_switch.hostname, thread))
                self.logger.debug(
                    f"Add ACI switch '{aci_switch.hostname}' to thread successfully."
                )

        for _, thread in fabric_bootstrap_threads:
            thread.start()

        for _, thread in fabric_bootstrap_threads:
            thread.join()

        install_errors = []
        for hostname, thread in fabric_bootstrap_threads:
            if thread.get_result():
                self.logger.info(f"Install '{hostname}' successfully.")
            else:
                self.logger.error(
                    f"Install '{hostname}' failed. Check APIC/switch logs for details."
                )
                install_errors.append(hostname)

        if install_errors:
            self.logger.error(
                "ACI fabric bootstrap failed, check APIC/switch logs for details."
            )
            return False

        self.logger.info("ACI fabric bootstrap successfully.")
        return True

    def apic_init_setup(self):
        """
        Method: 02-apic_init_setup
        Description: APIC initial setup (Single Pod)
        """

        self.logger.info("Start to initial setup APIC...")

        fabric_policy = self.global_policy.get("fabric", {})
        global_policies = fabric_policy.get("global_policies", {}) or {}
        apic_check = "apic_nodes_connection" in fabric_policy

        # Validate APIC exists
        if apic_check:
            apics = fabric_policy.get("apic_nodes_connection", []) or []

            for apic_cimc_connection in apics:
                apic = ApicCimcTool(global_policies, apic_cimc_connection, apics)
                if not apic.api_validate_apic():
                    self.logger.error(f"Validate APIC CIMC'{apic.hostname}' failed!")
                    return False
                self.logger.info(f"Validate APIC CIMC {apic.hostname} successfully.")

            for apic_cimc_connection in apics:
                if settings.APIC_DISCOVER_SKIP_FLAG:
                    self.logger.info(f"Skip APIC discovery for {apic.hostname}.")
                    break
                apic = ApicCimcTool(global_policies, apic_cimc_connection, apics)
                if not apic.ssh_init_apic():
                    self.logger.error(f"Initial setup APIC '{apic.hostname}' failed!")
                    return False
                self.logger.info(f"Initial setup APIC {apic.hostname} successfully.")
        else:
            self.logger.error("No APIC found!")
            return False

        return True

    def _load_aac_data(self):
        """Load global policy and AAC data"""

        self.logger.debug("Loading global policy and AAC data...")

        try:
            if self.yaml_tool.render_j2_templates(
                settings.TEMPLATE_DIR.get("nac_tasks")
            ):
                self.logger.debug(
                    f"Generate AAC working directory: '{self.output_path}' successfully."
                )

            nac_data_path = os.path.join(self.data_path, "nac_data")
            nac_data = YamlTool(data_path=nac_data_path)
            nac_data_yaml = nac_data.load_yaml_files()

            aac_path = os.path.join(
                self.output_path,
                os.path.basename(settings.TEMPLATE_DIR.get("nac_tasks")),
                "host_vars",
                "apic1",
            )
            aac_data_path = os.path.join(aac_path, "data.yaml")

            with open(aac_data_path, "w") as aac:
                y = yaml.YAML()
                y.default_flow_style = False
                y.dump(nac_data_yaml, aac)

            self.logger.debug(
                f"Copy NAC data to working directory: '{self.aac_data_path}' successfully."
            )

            self.aac_inventory_path = os.path.join(
                os.getcwd(),
                self.output_path,
                os.path.basename(settings.TEMPLATE_DIR.get("nac_tasks")),
                "inventory.yaml",
            )

            self.logger.debug("Set AAC inventory successfully.")
            return True

        except Exception as e:
            self.logger.error(f"Exception occurred during loading AAC data: {str(e)}")
            self.logger.error(traceback.format_exc())

        return False

    def apic_nac_config(self):
        """
        Method: 03-apic_nac_config
        Description: Init ACI Fabric via NaC (Network as Code)
        """

        self.logger.debug("Start to configure ACI Fabric via NaC...")

        fabric_policy = self.global_policy.get("fabric", {})
        global_policies = fabric_policy.get("global_policies", {}) or {}
        apic_check = "apic_nodes_connection" in fabric_policy

        # Validate APIC exists
        if apic_check:
            apics = fabric_policy.get("apic_nodes_connection", []) or []
            apic1 = next((apic for apic in apics if apic.get("id") == 1), None)
            if not apic1:
                self.logger.error("No APIC1 found!")
        else:
            self.logger.error("No APIC found!")
            return False

        apic = ApicTool(global_policies, apic1)
        if not apic.api_validate_apic():
            self.logger.error(f"Validate APIC '{apic.hostname}' failed!")
            return False
        self.logger.info(f"Validate APIC {apic.hostname} successfully.")

        if not self._load_aac_data():
            self.logger.error("Failed to load AAC data!")
            return False

        aac_ansible = AnsibleTool(self.output_path)

        playbook_dir_validate = os.path.join(
            os.getcwd(),
            self.output_path,
            os.path.basename(settings.TEMPLATE_DIR.get("nac_tasks")),
            "aac_ansible",
            "apic_validate.yaml",
        )

        if not aac_ansible.ansible_runner(
            "validate", playbook_dir_validate, self.aac_inventory_path
        ):
            self.logger.error("ACI as Code validation failed!")
            return False

        playbook_dir_deploy = os.path.join(
            os.getcwd(),
            self.output_path,
            os.path.basename(settings.TEMPLATE_DIR.get("nac_tasks")),
            "aac_ansible",
            "apic_deploy.yaml",
        )

        if not aac_ansible.ansible_runner(
            "deploy", playbook_dir_deploy, self.aac_inventory_path
        ):
            self.logger.error("ACI as Code deploy failed!")
            return False

        playbook_dir_test = os.path.join(
            os.getcwd(),
            self.output_path,
            os.path.basename(settings.TEMPLATE_DIR.get("nac_tasks")),
            "aac_ansible",
            "apic_test.yaml",
        )

        if not aac_ansible.ansible_runner(
            "test", playbook_dir_test, self.aac_inventory_path
        ):
            self.logger.error("ACI as Code test failed!")
            return False

        self.logger.info(f"Configure APIC {apic.hostname} via AAC successfully.")
        return True
