# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Wang Xiao <xiawang3@cisco.com>

import os.path
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
base_dir = f"aac_init_output_working_dir_{current_datetime}"

OUTPUT_BASE_DIR = os.path.join(os.getcwd(), base_dir)

DEFAULT_USER_SELECTIONS = [
    "Wipe and boot APIC/switch to particular version",
    "APIC initial setup (Single Pod)",
    "Init ACI Fabric via NaC (Network as Code)"
]


DEFAULT_DATA_PATH = ["00-global_policy.yml", "00-global_policy.yaml"]
DEFAULT_FABRIC_MGMT_PATH = ["01-fabric_mgmt.yml", "01-fabric_mgmt.yaml"]
DATA_PATH = "nac_data"

SCHEMA_DIR = os.path.join(BASE_DIR, "schemas")

# TEMPLATE_DIR = [
#     os.path.join(BASE_DIR, "templates", "03-nac_tasks"),
# ]

TEMPLATE_DIR = {
    "nac_tasks": os.path.join(BASE_DIR, "templates", "03-nac_tasks"),
}

# OUTPUT_DIR = [
#     os.path.join(OUTPUT_BASE_DIR, "01-fabric_bootstrap"),
#     os.path.join(OUTPUT_BASE_DIR, "02-apic_setup"),
#     os.path.join(OUTPUT_BASE_DIR, "03-nac_tasks"),
# ]

# os.environ["aac_init_option_1"] = OUTPUT_DIR[0]
# os.environ["aac_init_option_2"] = OUTPUT_DIR[1]


# STEP_1_YAML_LIST = []
# STEP_2_YAML_LIST = []

# YAML_NAME = [
#     ['playbook_apic_bootstrap.yaml', 'playbook_aci_switch_bootstrap.yaml'],
#     'playbook_apic_setup.yaml'
# ]

# ANSIBLE_STEP = [
#     'apic_bootstrap',
#     'aci_switch_bootstrap',
#     'apic_setup',
#     'aac_validate',
#     'aac_deploy',
#     'aac_test'
# ]

DEFAULT_LOG_LEVEL = 'info'

APIC_DISCOVER_SKIP_FLAG = False # Not skip APIC discovery by default, set to True for APIC2/3 on version 6.x
