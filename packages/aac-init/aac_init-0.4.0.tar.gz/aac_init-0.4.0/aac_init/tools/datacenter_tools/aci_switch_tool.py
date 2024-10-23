# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Rudy Lei <shlei@cisco.com>, Yang Bian <yabian@cisco.com>, Wang Xiao <xiawang3@cisco.com>

import re
import ipaddress
import traceback

from aac_init.log_utils import setup_logger, netmiko_session_logger
from netmiko import ConnectHandler
from time import sleep


class AciSwitchTool:
    """ACI Switch Toolkits, include Telnet and SSH."""

    def __init__(
        self, global_policies: dict, switch_connection: dict, fabric_mgmt_node: dict
    ):
        for k, v in global_policies.items():
            setattr(self, k, v)
        for k, v in switch_connection.items():
            setattr(self, k, v)
        for k, v in fabric_mgmt_node.items():
            setattr(self, k, v)

        self.logger = setup_logger(f"aciswitchtool_{self.hostname}.log")
        self.switch_telnet = {
            "host": self.console_address,
            "port": self.console_port,
            "username": self.aci_local_username,
            "password": self.aci_local_password,
            "session_log": netmiko_session_logger(
                f"telnet_session_{self.hostname}.log"
            ),
            "session_log_file_mode": "append",
        }
        self.telnet_connection = None

        self.switch_standby_telnet = {}
        if hasattr(self, "console_address_standby") and hasattr(
            self, "console_port_standby"
        ):
            self.switch_standby_telnet = {
                "host": self.console_address_standby,
                "port": self.console_port_standby,
                "username": self.aci_local_username,
                "password": self.aci_local_password,
                "session_log": netmiko_session_logger(
                    f"telnet_session_{self.hostname}_standby.log"
                ),
                "session_log_file_mode": "append",
            }
        self.telnet_connection_standby = None

        self.aci_version = None
        self.aci_switch_workflow = (
            0  # ACI switch validation, installation workflow protection
        )

        self.logger.debug("ACI switch tool initialized successfully.")

    def _telnet_connect(self):
        """Telnet Connector"""

        DEVICE_TYPES = [
            "cisco_ios_telnet",
            "generic_telnet",
        ]

        for i in range(1, 4):
            for device_type in DEVICE_TYPES:
                try:
                    self.logger.debug(
                        f"Attempting to connect '{self.hostname}' via telnet '{self.console_address}:{self.console_port}' with '{device_type}'..."
                    )
                    self.switch_telnet["device_type"] = device_type
                    self.telnet_connection = ConnectHandler(**self.switch_telnet)
                    self.logger.debug(
                        f"Connected to '{self.console_address}:{self.console_port}' with '{device_type}' successfully!"
                    )
                    return True
                except Exception as e:
                    self.logger.warning(
                        f"Failed to connect to '{self.console_address}:{self.console_port}' with '{device_type}': {e}"
                    )
                    self.logger.warning(traceback.format_exc())
                    sleep(3)

            self.logger.warning(
                f"Failed to connect to '{self.console_address}:{self.console_port}' with both telnet methods! Retry = {i}"
            )

        self.logger.error(
            f"Failed to connect to '{self.console_address}:{self.console_port}' with both telnet methods after 3 attempts!"
        )
        return False

    def _telnet_connect_standby(self):
        """Telnet Connector for standby"""

        DEVICE_TYPES = [
            "cisco_ios_telnet",
            "generic_telnet",
        ]

        for i in range(1, 4):
            for device_type in DEVICE_TYPES:
                try:
                    self.logger.debug(
                        f"Attempting to connect {self.hostname}_standby via telnet {self.console_address_standby}:{self.console_port_standby} with {device_type}..."
                    )
                    self.switch_telnet["device_type"] = device_type
                    self.telnet_connection_standby = ConnectHandler(
                        **self.switch_standby_telnet
                    )
                    self.logger.debug(
                        f"Connected to '{self.console_address_standby}:{self.console_port_standby}' with '{device_type}' successfully!"
                    )
                    return True
                except Exception as e:
                    self.logger.warning(
                        f"Failed to connect to '{self.console_address_standby}:{self.console_port_standby}' with '{device_type}': {e}"
                    )
                    self.logger.warning(traceback.format_exc())
                    sleep(3)

            self.logger.warning(
                f"Failed to connect to '{self.console_address_standby}:{self.console_port_standby}' with both telnet methods! Retry = {i}"
            )

        self.logger.error(
            f"Failed to connect to '{self.console_address_standby}:{self.console_port_standby}' with both telnet methods after 3 attempts!"
        )
        return False

    def _telnet_disconnect(self):
        if self.telnet_connection:
            self.telnet_connection.disconnect()
            sleep(3)  # Safely release console
            self.logger.debug(f"Disconnected telnet connection for: {self.hostname}")
            return True
        else:
            self.logger.error(f"No telnet connection found: {self.hostname}")
            return False

    def _telnet_disconnect_standby(self):
        if self.telnet_connection_standby:
            self.telnet_connection_standby.disconnect()
            sleep(3)  # Safely release console
            self.logger.debug(
                f"Disconnected standby telnet connection for: {self.hostname}"
            )
            return True
        else:
            self.logger.error(f"No standby telnet connection found: {self.hostname}")
            return False

    def _validate_aci_switch_image(self):
        """Validate ACI switch image"""

        self.logger.debug("Validating ACI switch image...")
        pattern = r"(?:aci-n9000-dk9\.)(\d+\.\d+\.\d+[a-z])\.bin"
        version_match = re.search(pattern, self.switch_image)

        if version_match:
            self.logger.debug(
                f"Validate version: '{version_match.group(1)}' successfully."
            )
            version_part = re.match(
                r"(\d+)\.(\d+)\.(\d+)([a-z])", version_match.group(1)
            )

            if version_part:
                major, minor, patch, _ = version_part.groups()
                self.aci_version = [int(major), int(minor), int(patch)]
                self.logger.debug(f"ACI version: {self.aci_version}")
                return True
            else:
                self.logger.error("Failed to parse the version components!")
        else:
            self.logger.error("Invalid ACI switch image format!")

        return False

    def _telnet_validate_aci_switch(self, telnet_connection):
        """
        1. Validate ACI switch image.
        2. Validate ACI switch based on switch prompt:
            - loader: not supported for version 16.0.2 and later, warning if no 'keyinfo'
            - nxos/aci with N9K PID: pass
        """

        self.logger.debug(f"Validating ACI switch: {self.hostname}")

        self._validate_aci_switch_image()
        if not self.aci_version:
            self.logger.error(
                "Validate ACI switch failed due to image validation failed!"
            )
            return False

        try:
            switch_prompt = telnet_connection.find_prompt(delay_factor=60)
            self.logger.debug(f"switch prompt: {switch_prompt}")

            if "loader >" in switch_prompt:
                loader_output = telnet_connection.send_command_timing("keyinfo")
                if self.aci_version >= [16, 0, 2]:
                    self.logger.error(
                        f"Selected ACI version is {self.aci_version}, cannot determine memory information under loader mode!"
                    )
                    return False

                if "Nexus9k" in loader_output:
                    self.aci_switch_workflow = 2
                    self.logger.debug(
                        "Nexus9k identified in loader output. Loader validated successfully."
                    )
                    return True

                else:
                    # TODO: Need to enhance loader handle in further version
                    self.logger.warning(
                        "N9K not found in loader output or 'keyinfo' not supported in this loader version. Manual intervention required."
                    )
                    self.logger.warning(
                        "Beta behavior: aac-init will keep install ACI image, but it might be failed..."
                    )
                    self.aci_switch_workflow = 2
                    return True

            elif "#" in switch_prompt:
                version_output = telnet_connection.send_command(
                    "show version | grep kickstart"
                )
                inventory_output = telnet_connection.send_command(
                    "show inventory | grep -A1 Chassis"
                )

                if (
                    "aci" in version_output or "nxos" in version_output
                ) and "N9K" in inventory_output:
                    self.aci_switch_workflow = 1
                    self.logger.debug(
                        "ACI/NXOS image and N9K chassis identified. Switch validated successfully."
                    )
                    return True

                else:
                    self.logger.error(
                        "Switch validation failed! ACI/NXOS or N9K not detected!"
                    )

            else:
                self.logger.error(
                    "Unrecognized device prompt. Unable to validate the switch!"
                )

        except Exception as e:
            # Log any exceptions that occur during the validation process
            self.logger.error(
                f"Exception occurred during validation for aci switch: {str(e)}"
            )
            self.logger.error(traceback.format_exc())

        finally:
            if telnet_connection == self.telnet_connection:
                self._telnet_disconnect()
            elif telnet_connection == self.telnet_connection_standby:
                self._telnet_disconnect_standby()
            else:
                self.logger.error(
                    f"Unknown telnet connection: {str(telnet_connection)}"
                )

        return False

    def _telnet_set_loader(self, telnet_connection):
        """Set N9K switch to loader mode"""

        # ACI switch validation is required before set loader
        if self.aci_switch_workflow not in [1, 2]:
            self.logger.error("ACI switch validation is not performed, aborting...")
            return False

        self.logger.debug(f"Setting '{self.hostname}' to loader...")

        try:
            switch_prompt = telnet_connection.find_prompt(delay_factor=60)
            self.logger.debug(f"switch prompt: {switch_prompt}")

            if "loader >" in switch_prompt:
                self.logger.debug("Already in loader.")
                return True

            # TODO: Need to enhance to determine ACI/NXOS running method on modular spine
            current_os_running = telnet_connection.send_command(
                "show version | grep kickstart", read_timeout=60
            )
            current_os_running += telnet_connection.send_command(
                "cat /mnt/cfg/0/boot/grub/menu.lst.local", read_timeout=60
            )

            # TODO: Always go 32-bit image for less 602, for 602 and above, install 64-bit per pid
            # TODO: Need to determine leaf memory selection..
            if self.aci_version >= [16, 0, 2]:
                SWITCH_602_64BIT = [
                    "N9K-C9408",
                    "N9K-C9504",
                    "N9K-C9508",
                    "N9K-C9516",
                    "N9K-C9364D-GX2A",
                    "N9K-C9348D-GX2A",
                    "N9K-C9332D-GX2B",
                    "N9K-C93600CD-GX",
                    "N9K-C9316D-GX",
                    "N9K-C9364C",
                ]
                pid_raw = telnet_connection.send_command(
                    "show inventory | grep -A1 Chassis", read_timeout=60
                )
                pid_pattern = re.compile(r"PID: (N9K-[A-Z0-9\-]+)")

                if pid_raw:
                    if not pid_pattern.findall(pid_raw):
                        self.logger.error(
                            f"Unable to determine chassis PID! PID raw output:\n {pid_raw}"
                        )
                        return False
                    if pid_pattern.findall(pid_raw)[0] in SWITCH_602_64BIT:
                        self.switch_image = self.switch_image.replace(
                            ".bin", "-cs_64.bin"
                        )
                        self.logger.debug(f"Target image: {self.switch_image}")
                else:
                    # TODO: Need to enhance to determine modular spine
                    # No pid_raw output for standby sup of modular spine, set to 64-bit directly.
                    self.switch_image = self.switch_image.replace(".bin", "-cs_64.bin")
                    self.logger.debug(f"Target image: {self.switch_image}")

            # ACI handler
            if "aci" in current_os_running:
                self.logger.debug("ACI OS handling...")
                telnet_connection.send_command("rm -f bootflash/*.bin", read_timeout=90)
                telnet_connection.send_command(
                    "setup-clean-config.sh", "Done", read_timeout=180
                )
                telnet_connection.send_command(
                    "clear-bootvars.sh", "Done", read_timeout=180
                )

                grub0_output = telnet_connection.send_command(
                    "ls /mnt/cfg/0/boot/grub/"
                )
                grub1_output = telnet_connection.send_command(
                    "ls /mnt/cfg/1/boot/grub/"
                )
                # match file/folder
                file_pattern = re.compile(
                    r"^[\w\-\.\s\u4e00-\u9fff\u3040-\u30ff\u00a1-\uffff]+$"
                )
                grub0_files = [
                    line
                    for line in grub0_output.splitlines()
                    if file_pattern.match(line)
                ]
                grub1_files = [
                    line
                    for line in grub1_output.splitlines()
                    if file_pattern.match(line)
                ]
                if grub0_files or grub1_files:
                    self.logger.error("Clear grub failed!")
                    return False

                self.logger.debug("GRUB cleared, entering loader...")
                telnet_connection.send_command(
                    "reload", "This command will reload the chassis", read_timeout=60
                )
                telnet_connection.send_command_timing("y")

                telnet_connection.read_until_pattern(
                    pattern="loader >", read_timeout=300
                )

            # Nexus handler
            else:
                self.logger.debug("NXOS handling...")
                telnet_connection.send_command(
                    "configure terminal", "config", read_timeout=60
                )
                telnet_connection.send_command(
                    "delete bootflash:*.bin no-prompt", read_timeout=60
                )
                telnet_connection.send_command("no boot nxos", read_timeout=60)
                telnet_connection.send_command(
                    "copy running-config startup-config",
                    "Copy complete.",
                    read_timeout=60,
                )
                telnet_connection.send_command(
                    "reload", "This command will reboot the system", read_timeout=60
                )
                telnet_connection.send_command_timing("y")
                telnet_connection.read_until_pattern(
                    pattern="loader >", read_timeout=300
                )

            self.aci_switch_workflow = 2
            self.logger.debug("Entered to loader.")
            return True

        except Exception as e:
            # Log any exceptions that occur during the set loader process
            self.logger.error(
                f"Exception occurred during set loader for aci switch: {str(e)}"
            )
            self.logger.error(traceback.format_exc())

        finally:
            if telnet_connection == self.telnet_connection:
                self._telnet_disconnect()
            elif telnet_connection == self.telnet_connection_standby:
                self._telnet_disconnect_standby()
            else:
                self.logger.error(
                    f"Unknown telnet connection: {str(telnet_connection)}"
                )

        return False

    def _telnet_loader_install_aci_switch(self, telnet_connection):
        """Install aci switch from loader mode"""

        # loader is required to install aci switch
        if self.aci_switch_workflow != 2:
            self.logger.error(
                "ACI switch validation or set loader is required before installation, aborting..."
            )
            return False

        self.logger.debug(f"Installing '{self.hostname}' from loader...")

        aci_switch_image_http = self.aci_image_path + self.switch_image
        aci_switch_image_tftp = aci_switch_image_http.replace("http", "tftp")
        self.logger.debug(f"ACI switch image tftp path: {aci_switch_image_tftp}")

        device_oob_trad = ipaddress.IPv4Interface(self.oob_address)
        set_tftp_ip = f"set ip {device_oob_trad.ip} {device_oob_trad.netmask}"
        set_tftp_gw = f"set gw {self.oob_gateway}"
        tftp_boot_cmd = f"boot {aci_switch_image_tftp}"

        try:
            telnet_connection.send_command_timing("\n")
            telnet_connection.send_command_timing(set_tftp_ip)
            set_gw_result = telnet_connection.send_command_timing(set_tftp_gw)

            address_check = f"Address: {device_oob_trad.ip}" in set_gw_result
            netmask_check = f"Netmask: {device_oob_trad.netmask}" in set_gw_result
            gateway_check = f"Gateway: {self.oob_gateway}" in set_gw_result

            if all([address_check, netmask_check, gateway_check]):
                telnet_connection.send_command_timing(tftp_boot_cmd)
                self.logger.debug(
                    (
                        f"Node '{self.hostname}': Starting to install '{self.switch_image}'"
                    )
                )
                telnet_connection.read_until_pattern(
                    pattern="Certificate verification passed", read_timeout=900
                )

                # loader post-installation check
                sleep(180)
                post_check_result = telnet_connection.send_command_timing("\n")
                version_post_check = re.search(
                    r"aci-n9000-dk9\.\d+\.\d+\.\d+[a-z]", self.switch_image
                ).group(0)

                for i in range(1, 31):
                    self.logger.debug(f"Post check retry: {i}")
                    self.logger.debug(post_check_result)
                    if "(none) login:" in telnet_connection.find_prompt(
                        delay_factor=60
                    ):
                        post_check_result = telnet_connection.send_command_timing(
                            "admin"
                        )

                    elif "(none)#" in telnet_connection.find_prompt(delay_factor=60):
                        post_check_result = telnet_connection.send_command(
                            "cat /mnt/cfg/0/boot/grub/menu.lst.local",
                            expect_string=version_post_check,
                            read_timeout=60,
                        )
                        self.logger.debug(
                            f"ACI switch successfully installed {self.switch_image}"
                        )

                        return True

                    else:
                        post_check_result = telnet_connection.send_command_timing("\n")
                        sleep(1)

                self.logger.error("ACI switch installation post-check timeout!")
            else:
                self.logger.error("set_gw_result check failed!")

        except Exception as e:
            # Log any exceptions that occur during the set loader process
            self.logger.error(
                f"Exception occurred during set loader for aci switch: {str(e)}"
            )
            self.logger.error(traceback.format_exc())

        finally:
            if telnet_connection == self.telnet_connection:
                self._telnet_disconnect()
            elif telnet_connection == self.telnet_connection_standby:
                self._telnet_disconnect_standby()
            else:
                self.logger.error(
                    f"Unknown telnet connection: {str(telnet_connection)}"
                )

        return False

    def validate_aci_switch(self):
        """
        Validate ACI switch by performing the following steps:
        1. Validate switch active console
        2. Validate switch standby console if modular spine(Opt)
        """

        self.logger.debug(f"Validating ACI switch: {self.hostname}")

        if not self._telnet_connect():
            self.logger.error(
                f"Validating ACI switch '{self.hostname}' failed due to console login failed!"
            )
            return False

        if self._telnet_validate_aci_switch(self.telnet_connection):
            self.logger.debug(f"ACI switch '{self.hostname}' validated successfully.")
        else:
            self.logger.error(f"Failed to validate ACI switch '{self.hostname}'!")
            return False

        # Validate Standby sup for modular spine if have
        if self.switch_standby_telnet:
            if not self._telnet_connect_standby():
                self.logger.error(
                    f"Validating ACI switch '{self.hostname}_standby' failed due to console login failed!"
                )
                return False

            if self._telnet_validate_aci_switch(self.telnet_connection_standby):
                self.logger.debug(
                    f"ACI switch '{self.hostname}_standby' validated successfully."
                )
            else:
                self.logger.error(
                    f"Failed to validate ACI switch '{self.hostname}_standby'!"
                )
                return False

        return True

    def install_aci_switch(self):
        """
        Install ACI switch by performing the following steps:
        1. Set switch active console to loader
        2. Set switch standby console to loader if modular spine(Opt)
        3. Install switch active console
        4. Install switch standby console if modular spine(Opt)
        """

        self.logger.debug(f"Installing ACI switch: '{self.hostname}'...")

        if not self._telnet_connect():
            self.logger.error(
                f"Install ACI switch '{self.hostname}' failed due to console login failed!"
            )
            return False

        if self._telnet_set_loader(self.telnet_connection):
            self.logger.debug(
                f"Setting ACI switch '{self.hostname}' to loader successfully."
            )
        else:
            self.logger.error(f"Failed to set ACI switch '{self.hostname}' to loader!")
            return False

        # Set Standby sup to loader for modular spine if have
        if self.switch_standby_telnet:
            if not self._telnet_connect_standby():
                self.logger.error(
                    f"Install ACI switch '{self.hostname}_standby' failed due to console login failed!"
                )
                return False

            if self._telnet_set_loader(self.telnet_connection_standby):
                self.logger.debug(
                    f"ACI switch '{self.hostname}_standby' set loader successfully."
                )
            else:
                self.logger.error(
                    f"Failed to set ACI switch '{self.hostname}_standby' to loader!"
                )
                return False

        if not self._telnet_connect():
            self.logger.error(
                f"Install ACI switch '{self.hostname}' failed due to console login failed!"
            )
            return False

        if self._telnet_loader_install_aci_switch(self.telnet_connection):
            self.logger.info(
                f"Install ACI switch '{self.hostname}' to '{self.switch_image}' successfully."
            )
        else:
            self.logger.error(
                f"Failed to install ACI switch '{self.hostname}' to '{self.switch_image}'!"
            )
            return False

        # Install Standby sup for modular spine if have
        if self.switch_standby_telnet:
            if not self._telnet_connect_standby():
                self.logger.error(
                    f"Install ACI switch '{self.hostname}_standby' failed due to console login failed!"
                )
                return False

            if self._telnet_loader_install_aci_switch(self.telnet_connection_standby):
                self.logger.info(
                    f"Install ACI switch '{self.hostname}_standby' to '{self.switch_image}' successfully."
                )
            else:
                self.logger.error(
                    f"Failed to install ACI switch '{self.hostname}_standby' to '{self.switch_image}'!"
                )
                return False

        return True
