# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

"""
Entrypoint for TRT Cloud CLI.
"""

import argparse
import logging
import os
import sys
from typing import List, Optional

import trt_cloud.subcommands
from trt_cloud.client import BuilderFunctionException
from trt_cloud.constants import ENGINE_LICENSE_PATH, LICENSE_PATH
from trt_cloud.state import TRTCloudConfig
from trt_cloud.utils import add_verbose_flag_to_parser, check_and_display_eula

DISABLE_LICENSE_CHECK = os.getenv("TRTC_AGREE_TO_LICENSE") == "true"


def make_parser(subcommands):
    parser = argparse.ArgumentParser(description="TensorRT Cloud CLI")
    parser.add_argument("--version", action="version", version=trt_cloud.__version__)
    add_verbose_flag_to_parser(parser)

    command_names = [command for command in subcommands.keys() if command != 'unlock-ea']
    all_commands_str = "{" + ','.join(command_names) + "}"

    # Create a subparsers object to handle subcommands
    subparsers = parser.add_subparsers(
        title="Subcommands",
        dest="subcommand",
        metavar=all_commands_str,
        required=True
    )

    for subcommand_name, subcommand in subcommands.items():
        subparser = subcommand.add_subparser(subparsers, subcommand_name)
        add_verbose_flag_to_parser(subparser)

    return parser


def should_do_license_check(args, trtc_config, subcommand) -> bool:
    if DISABLE_LICENSE_CHECK:
        return False
    elif trtc_config.agreed_to_license(trt_cloud.__version__):
        return False
    else:
        return subcommand.prompt_license


def should_do_engine_license_check(args, trtc_config, subcommand) -> bool:
    if not isinstance(subcommand, trt_cloud.subcommands.CatalogSubcommand):
        return False
    elif DISABLE_LICENSE_CHECK:
        return False
    elif trtc_config.agreed_to_engine_license(trt_cloud.__version__):
        return False
    else:
        return True


def main(run_opts: Optional[List[str]] = None):
    logging.basicConfig(format='[%(levelname).1s] %(message)s', level=logging.INFO)
    trtc_config = TRTCloudConfig()

    subcommands = {
        "catalog": trt_cloud.subcommands.CatalogSubcommand,
        "unlock-ea": trt_cloud.subcommands.UnlockSubcommand,
    }
    if trtc_config.are_all_commands_unlocked() or os.getenv("TRTC_UNLOCK_EA_SUBCOMMANDS"):
        subcommands.update({
            "login": trt_cloud.subcommands.LoginSubcommand,
            "info": trt_cloud.subcommands.InfoSubcommand,
            "build": trt_cloud.subcommands.BuildSubcommand,
            "refit": trt_cloud.subcommands.RefitSubcommand,
        })

    parser = make_parser(subcommands)
    if run_opts is not None:
        args = parser.parse_args(run_opts)
    else:
        args = parser.parse_args()

    if hasattr(args, "verbose") and args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    try:
        subcommand = subcommands[args.subcommand]()

        if should_do_license_check(args, trtc_config, subcommand):
            if check_and_display_eula(LICENSE_PATH, eula_name="TRT Cloud EULA") and \
                    check_and_display_eula(ENGINE_LICENSE_PATH, eula_name="TRT Cloud Engine EULA"):
                trtc_config.save_agreed_to_license(trt_cloud.__version__)

        if should_do_engine_license_check(args, trtc_config, subcommand):
            if check_and_display_eula(ENGINE_LICENSE_PATH, eula_name="TRT Cloud Engine EULA"):
                trtc_config.save_agreed_to_engine_license(trt_cloud.__version__)

        subcommand.run(args)
    except ValueError as e:
        logging.error(str(e))
        sys.exit(1)
    except BuilderFunctionException as e:
        logging.error(str(e))
        sys.exit(2)
