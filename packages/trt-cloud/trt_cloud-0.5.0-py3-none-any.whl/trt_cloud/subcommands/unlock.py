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

from trt_cloud.state import TRTCloudConfig
from trt_cloud.subcommands.base_subcommand import Subcommand


class UnlockSubcommand(Subcommand):

    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'unlock-ea' subcommand to the main CLI argument parser.
        """
        info_subcommand = subparsers.add_parser(subcommand_name)

        return info_subcommand

    def run(self, args):
        """
        Execute the 'unlock-ea' subcommand. It does not have any args.
        """
        TRTCloudConfig().unlock_all_commands()
        logging.info("Unlocked all subcommands.")
