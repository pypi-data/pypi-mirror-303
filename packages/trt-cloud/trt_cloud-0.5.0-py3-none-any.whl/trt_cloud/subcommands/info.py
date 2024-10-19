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

from tabulate import tabulate

from trt_cloud.client import TRTCloud
from trt_cloud.subcommands.base_subcommand import Subcommand


class InfoSubcommand(Subcommand):

    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'info' subcommand to the main CLI argument parser.
        """
        info_subcommand = subparsers.add_parser(
            subcommand_name, help="Get the list of available GPUs."
        )

        return info_subcommand

    def run(self, args):
        """
        Execute the 'info' subcommand. It does not have any args.
        """
        trtcloud = TRTCloud()
        funcs = trtcloud.get_available_functions()

        if not funcs:
            logging.warning("No builders currently available on TRT Cloud")
            return

        funcs.sort(
            key=lambda f: (
                f.os,
                f.gpu,
                # empty tags appear first
                len(f.tags),
                f.tags,
            )
        )

        table_headers_short = ["OS", "GPU", "TRT Versions (for ONNX builds)", "TRT-LLM Versions", "Command"]
        table_data_short = []
        table_data_verbose = []

        for func in funcs:
            # Skip non-latest versions by default
            if not func.is_latest:
                continue

            trt_versions = func.trt_versions
            if trt_versions:
                trt_versions = ", ".join(trt_versions)

            trtllm_versions = func.trtllm_versions
            if trtllm_versions:
                trtllm_versions = ", ".join(trtllm_versions)

            # tags, excluding the OS and GPU
            tags = [t for t in func.tags if not t.startswith(("os=", "gpu=", "trt_versions=", "trtllm_version="))]

            # command to run the function; start with OS and GPU, then add tags if any
            command = "--os={os} --gpu={gpu} {tags}".format(
                os=func.os,
                gpu=func.gpu,
                tags="".join(
                    f'--tag "{t}" ' if " " in t else f"--tag {t} " for t in tags
                ),
            )

            row_short = [func.os.capitalize(), func.gpu, trt_versions, trtllm_versions, command]
            table_data_short.append(row_short)

            table_data_verbose.append([
                [f"{func.os.capitalize()} + {func.gpu}", ""],
                ["OS", func.os],
                ["GPU", func.gpu],
                ["TRT Versions (for ONNX builds)", trt_versions],
                ["TRT LLM Versions:", trtllm_versions],
                ["Tags:", " ".join(tags)],
                ["Command:", command],
                ["Created At:", func.created_at.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")],
                ["Function ID:", func.func_id],
                ["Version ID:", func.version_id],
            ])

        if args.verbose:
            table_str = "\n".join(
                tabulate(rows, headers="firstrow", tablefmt="simple_outline")
                for rows in table_data_verbose
            )
        else:
            table_str = tabulate(
                table_data_short,
                headers=table_headers_short,
                tablefmt="simple_outline",
            )

        logging.info("Available runners:\n" + table_str)
