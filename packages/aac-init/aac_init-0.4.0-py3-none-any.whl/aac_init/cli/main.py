# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Wang Xiao <xiawang3@cisco.com>, Rudy Lei <shlei@cisco.com>

import os
import re
import sys
import click
import shutil
import errorhandler
import time

from .. import __version__
from . import options, selections, cli_validators
from aac_init.conf import settings
from aac_init.log_utils import setup_logger


error_handler = errorhandler.ErrorHandler()


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__)
@options.yaml_dir_path
@options.log_level
def main(data: str, log_level: str) -> None:
    """
    A CLI tool to bootstrap and configure ACI fabric using ACI as Code.
    """
    # Setup working dir
    output_path = settings.OUTPUT_BASE_DIR

    if os.path.exists(output_path) and os.path.isdir(output_path):
        shutil.rmtree(output_path)

    settings.DEFAULT_LOG_LEVEL = log_level

    logger = setup_logger("main.log")

    cli_validator = cli_validators.CliValidator(data, output_path)
    logger.info("CLI Validator initialized.\n")

    # Type single number or multiple numbers (1,2... or *)
    selection_str = "\n".join(
        [
            f"[{i + 1}]  {selection}"
            for i, selection in enumerate(settings.DEFAULT_USER_SELECTIONS)
        ]
    )
    selection_prompt = (
        f"Select single or multiple choice(s) "
        f"to init ACI Fabric:\n{selection_str}\nExample: (1,2,.. or *)"
    )

    selection_choices = click.prompt(
        click.style(selection_prompt, fg="green"),
        type=cli_validator.validate_selections,
    )
    logger.info("Selections validated successfully.")

    if not selection_choices:
        logger.info("Selections validated failed. Exiting...")
        exit()

    # Type "yes" or "no" to confirm
    confirm_str = "\n".join(
        f"[{i}] {settings.DEFAULT_USER_SELECTIONS[int(i) - 1]}"
        for i in selection_choices
    )
    confirm_prompt = (
        f"\nAre you sure to proceed with the following choice(s)?\n{confirm_str}\n"
    )

    selections_confirm = click.prompt(
        click.style(confirm_prompt, fg="green"),
        type=click.Choice(["yes", "no"], case_sensitive=False),
        default="yes",
        show_default=True,
        show_choices=True,
    )

    if not re.match(r"yes", selections_confirm, re.IGNORECASE):
        logger.error("Process aborted, exiting aac-init tool...")
        exit()

    logger.info("Start to process aac-init tool!")
    logger.info("Validating input data files...")
    if cli_validator.validate_cli_input():
        logger.info("Input data files validated successfully.")
    else:
        logger.error("Input data files validated failed!")
        exit()

    # selections handling
    cli_selection = selections.Selections(data, output_path)
    for selection in selection_choices:
        logger.info(f"Start to process selection: {selection}")
        match selection:
            case "1":
                if cli_selection.fabric_bootstrap():
                    logger.info("ACI fabric bootstrap successfully.")
                else:
                    logger.error("ACI fabric bootstrap failed!")
                    exit()
            case "2":
                if cli_selection.apic_init_setup():
                    logger.info("APIC initial setup successfully.")
                else:
                    logger.error("APIC initial setup failed!")
                    exit()
            case "3":
                if "2" in selection_choices:
                    time.sleep(300)
                if cli_selection.apic_nac_config():
                    logger.info("Configure ACI fabric successfully.")
                else:
                    logger.error("Configure ACI fabric failed!")
                    exit()
            case _:
                logger.error(f"Unknown selection: '{selection}'!")
                exit()


def exit() -> None:
    if error_handler.fired:
        sys.exit(1)
    else:
        sys.exit(0)
