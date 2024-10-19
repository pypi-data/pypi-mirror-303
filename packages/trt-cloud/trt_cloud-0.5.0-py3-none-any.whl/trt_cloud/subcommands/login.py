# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import argparse
import logging
from argparse import ArgumentParser

from trt_cloud.state import CONFIG_FILE, TRTCloudConfig
from trt_cloud.subcommands.base_subcommand import Subcommand


class LoginSubcommand(Subcommand):

    def __init__(self):
        super().__init__(prompt_license=True)

    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'login' subcommand to the main CLI argument parser.
        """
        login_subcommand = subparsers.add_parser(
            subcommand_name,
            help="Provide credentials for using NVCF.",
            description="""
            Provide credentials for using NVCF.
            Valid credentials are an nvapi key OR a SSA (client_id, client_secret) pair.
            Specifying no arguments will start an interactive mode.
            """
        )
        login_subcommand.add_argument("--client-id", "-u", help="NVCF SSA Client ID")
        login_subcommand.add_argument("--client-secret", "-p", help="NVCF SSA Client Secret")
        login_subcommand.add_argument("--nvapi-key", help="nvapi key authorized to use NVCF.")

        return login_subcommand

    def run(self, args):
        """
        Execute the 'login' subcommand with the given args.

        The following usages are valid:
        - Specifying both args.client_id and args.client_secret
        - Specifying only args.nvapi_key
        - Empty args (this triggers an interactive login).

        Raises ValueError if args are invalid.
        """
        def usage():
            raise ValueError("Provide either client credentials or nvapi key, but not both.")

        trtcloud_config = TRTCloudConfig()

        if args.nvapi_key:
            if args.client_id or args.client_secret:
                usage()

            trtcloud_config.save_login(None, None, args.nvapi_key)
            logging.info("Saved nvapi key to %s.", CONFIG_FILE)
            return

        if args.client_id or args.client_secret:
            if args.nvapi_key:
                usage()

            if not (args.client_id and args.client_secret):
                raise ValueError("Please provide both the client ID and the client secret.")

            trtcloud_config.save_login(args.client_id, args.client_secret, None)
            logging.info("Saved client ID and secret to %s.", CONFIG_FILE)
            return

        # Interactive Mode
        cred_type = input('Please enter credential type ["ssa" or "nvapi_key"]: ')

        if cred_type == "nvapi_key":
            nvapi_key = input('Please enter value for nvapi_key: ')
            trtcloud_config.save_login(None, None, nvapi_key)
            logging.info("Saved nvapi key to %s.", CONFIG_FILE)
        elif cred_type == "ssa":
            client_id = input('Please enter value for client_id: ')
            client_secret = input('Please enter value for client_secret: ')
            trtcloud_config.save_login(client_id, client_secret, None)
            logging.info("Saved client ID and secret to %s.", CONFIG_FILE)
        else:
            raise ValueError(f"Unknown credential type: {cred_type}")
