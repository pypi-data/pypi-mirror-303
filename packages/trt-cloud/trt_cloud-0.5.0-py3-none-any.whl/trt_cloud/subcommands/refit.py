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
from argparse import ArgumentParser

from trt_cloud.build_spec.build_options import BuildType
from trt_cloud.refitter.refit_helper import RefitHelper
from trt_cloud.subcommands.base_subcommand import Subcommand


class RefitSubcommand(Subcommand):

    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'refit' subcommand to the main CLI argument parser.
        """
        refit_subcommand = subparsers.add_parser(subcommand_name, help="Refit a built weightless engine.")

        type_group = refit_subcommand.add_mutually_exclusive_group(required=True)
        type_group.add_argument("--onnx", help="Local filepath of ONNX model")
        type_group.add_argument("--llm", help="Local filepath of TRT-LLM checkpoint")
        refit_subcommand.add_argument("-e", "--engine", type=str, required=True,
                                      help="Local path of the weight-stripped engine / build output")
        refit_subcommand.add_argument("--vc", action="store_true",
                                      help="(* ONNX model only) Refit a Version Compatible engine"
                                           "(the engine was built with trtexec args --versionCompatible"
                                           "or --vc). This option uses the lean runtime to refit the engine.")
        refit_subcommand.add_argument("-o", "--out", type=str, required=True,
                                      help="Location to save the refitted engine")

        return refit_subcommand

    def run(self, args):
        """
        Execute the 'refit' subcommand with the given args.

        The 'refit' subcommand is used to refit a weightless engine build,

        Raises ValueError if args are invalid.
        """
        if args.onnx:
            model_path = args.onnx
            model_type = BuildType.ONNX
        elif args.llm:
            model_path = args.llm
            model_type = BuildType.TRT_LLM

        RefitHelper().refit(
            engine_path=args.engine,
            model_path=model_path,
            model_type=model_type,
            output_path=args.out,
            is_engine_vc=args.vc
        )
