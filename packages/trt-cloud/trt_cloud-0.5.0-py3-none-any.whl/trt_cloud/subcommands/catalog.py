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

import tabulate

from trt_cloud import TRTCloud
from trt_cloud.subcommands.base_subcommand import Subcommand
from trt_cloud.utils import add_verbose_flag_to_parser


class CatalogSubcommand(Subcommand):

    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'catalog' subcommand to the main CLI argument parser.
        """
        catalog_subcommand = subparsers.add_parser(subcommand_name, help="Download public TRT engines built by NVIDIA.")
        catalog_subparsers = catalog_subcommand.add_subparsers(
            title="Subcommands", dest="catalog_subcommand", required=True)

        catalog_models_subcommand = catalog_subparsers.add_parser(   # noqa
            "models", help="List models TRT engines are available for.")
        add_verbose_flag_to_parser(catalog_models_subcommand)

        catalog_engines_subcommand = catalog_subparsers.add_parser(
            "engines", help="List downloadable TRT engines.")
        add_verbose_flag_to_parser(catalog_engines_subcommand)

        for (arg, desc) in [
            ("--model", "The model glob pattern"),
            ("--trtllm_version", "TRT LLM version"),
            ("--os", "OS"),
            ("--gpu", "GPU"),
        ]:
            catalog_engines_subcommand.add_argument(
                arg, type=str, required=False, default=None, help=f"{desc} to filter engines by.")

        catalog_download_subcommand = catalog_subparsers.add_parser("download", help="Download a TRT engine.")
        catalog_download_subcommand.add_argument(
            "--model", required=True, help="The model to download a TRT engine for. "
                                           "(Note: This should match the exact model name)")
        catalog_download_subcommand.add_argument(
            "--version", required=True, help="The version of the model to download.")
        catalog_download_subcommand.add_argument(
            "-o", "--output", required=False, default=None, help="The output path to download the engine to.")

        return catalog_subcommand

    def run(self, args):
        """
        Execute the 'catalog' subcommand with the given args.

        The 'catalog' subcommand is used for querying and downloading public TensorRT engines
        which were built by NVIDIA.

        Raises ValueError if args are invalid.
        """
        client = TRTCloud()

        if args.catalog_subcommand == "engines":
            engines = client.get_prebuilt_engines(
                model_name=args.model,
                trtllm_version=args.trtllm_version,
                os_name=args.os,
                gpu=args.gpu,
                glob_match_model_name=True
            )

            if not engines:
                logging.info("Found 0 engines.")
                return

            logging.info(
                "Found %d engine%s.\n\n%s",
                len(engines),
                "" if len(engines) == 1 else "s",
                tabulate.tabulate(
                    [
                        engine.as_pretty_print_dict(include_all_headers=args.verbose)
                        for engine in sorted(engines, key=lambda x: x.id)
                    ],
                    headers="keys",
                )
            )

        elif args.catalog_subcommand == "models":
            models = client.get_prebuilt_models()
            logging.info(
                "Found %d models.\n\n%s",
                len(models),
                tabulate.tabulate({"Model Name": sorted(models)}, headers="keys")
            )

        elif args.catalog_subcommand == "download":
            client.download_prebuilt_engine(args.model, args.version, output_filepath=args.output)
