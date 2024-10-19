# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import abc
import argparse
from argparse import ArgumentParser


class Subcommand(abc.ABC):

    def __init__(self, prompt_license: bool = False):
        self.prompt_license = prompt_license

    @staticmethod
    @abc.abstractmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds this subcommand's parser and arguments to the main CLI argument parser.
        """

    @abc.abstractmethod
    def run(self, args):
        """
        Run this subcommand with the parsed CLI arguments.
        """
