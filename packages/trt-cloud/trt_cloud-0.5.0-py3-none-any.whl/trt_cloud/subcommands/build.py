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
from typing import List

from trt_cloud.build_spec.build_input_source import (HFCheckpointSource,
                                                     TokenizerSource,
                                                     TRTLLMCheckpointSource,
                                                     TRTLLMSpecSource)
from trt_cloud.build_spec.build_options import (BuildType,
                                                TRTLLMBuildReturnType,
                                                TRTLLMDtype,
                                                TRTLLMKVQuantizationType,
                                                TRTLLMQuantizationType)
from trt_cloud.build_spec.build_recipe import TRTLLMRecipe
from trt_cloud.client import TRTCloud
from trt_cloud.subcommands.base_subcommand import Subcommand
from trt_cloud.utils import (ModelLicenseFamily,
                             check_and_display_huggingface_repo_engine_eulas)


class BuildSubcommand(Subcommand):
    @staticmethod
    def _add_common_build_options(parser: argparse.ArgumentParser):
        # Valid for all 'build' commands
        parser.add_argument("-o", "--out", type=str,
                            help="File path to save the build result to.")

    @staticmethod
    def _add_common_onnx_and_llm_options(parser: argparse.ArgumentParser):
        # Valid for both 'onnx' and 'llm' commands
        parser.add_argument("--gpu", help="GPU model to build engine for")
        parser.add_argument(
            "--os", help="OS to build engine for", choices=["linux", "windows"]
        )
        parser.add_argument(
            "--tag",
            help="""\
                  Tags to filter the runners by (can be specified multiple times); \
                  please run 'trt-cloud info' for a list of available runners and their tags.\
                  """,
            dest="tags",
            nargs="*",
            default=[],
        )
        parser.add_argument("--strip-weights", action='store_true',
                            help="Build a weight-stripped engine. "
                                 "This will prune weights from the model locally before uploading "
                                 "(unless the model is a from a url), "
                                 "and build a weight-stripped TensorRT engine.")
        parser.add_argument(
            "--local-refit", action='store_true',
            help="If set, will locally refit a weight-stripped engine after build. "
                 "Please make sure that your python environment has the TensorRT "
                 "version corresponding to the engine built."
        )
        parser.add_argument(
            "--function-id", "--function", help=argparse.SUPPRESS
        )
        parser.add_argument(
            "--function-version", "--function-version-id", help=argparse.SUPPRESS
        )
        BuildSubcommand._add_common_build_options(parser)

    @staticmethod
    def _add_onnx_build_options_to_parser(parser: argparse.ArgumentParser):
        # Valid for 'build onnx' commands
        parser.add_argument("--model", required=True,
                            help="URL or local filepath of ONNX model.")
        parser.add_argument(
            "--trt-version",
            default="latest",
            help="TRT Version to build the engine for. "
                 "May be \"latest\", \"default\", or a numeric version such as \"10.0\". "
                 "Only applicable for ONNX builds."
        )
        parser.add_argument("--trtexec-args", type=str, help="Args to pass to trtexec")
        BuildSubcommand._add_common_onnx_and_llm_options(parser)

    @staticmethod
    def _add_trtllm_build_options_to_parser(parser: argparse.ArgumentParser):
        # Valid for 'build trtllm' commands
        input_group = parser.add_mutually_exclusive_group(required=True)
        input_group.add_argument("--hf-repo", help="Huggingface repository.")
        parser.add_argument("--hf-repo-revision", help="Huggingface repository revision. "
                                                       "Only used if the input is a huggingface repository")
        input_group.add_argument("--trtllm-checkpoint",
                                 help="URL or local filepath containing TRT-LLM checkpoint config")
        parser.add_argument("--tokenizer", help="URL or local filepath containing a tokenizer. "
                                                "Only used for builds from TRT LLM checkpoints.")
        parser.add_argument("--return-type", type=TRTLLMBuildReturnType, help="Return type from build",
                            choices=list(TRTLLMBuildReturnType),
                            default=None)
        parser.add_argument(
            "--trtllm-version",
            default="latest",
            help="TRT LLM Version to build the engine for. "
                 "May be \"latest\" or a numeric version such as \"0.12.0\". "
                 "Only applicable for TRT LLM builds."
        )
        parser.add_argument("--dtype", type=TRTLLMDtype, choices=list(TRTLLMDtype), help="Data type.")
        parser.add_argument("--quantization", type=TRTLLMQuantizationType,
                            choices=list(TRTLLMQuantizationType),
                            default=TRTLLMQuantizationType.FULL_PREC, help="Quantization mode.")
        parser.add_argument("--quantize-kv-cache", action="store_true",
                            help="Use quantization for KV cache.")
        parser.add_argument("--max-input-len", type=int, default=None)
        parser.add_argument("--max-batch-size", type=int, default=None,
                            help="Max batch size defines the maximum number of requests that the engine can handle.")
        parser.add_argument("--max-seq-len", type=int, default=None,
                            help="Max sequence length defines the maximum sequence length of a single request.")
        parser.add_argument("--max-num-tokens", type=int, default=None,
                            help="Max num tokens defines the maximum number of batched input tokens "
                                 "after padding is removed in each batch.")
        parser.add_argument("--tp-size", type=int, default=1, choices=[1, 2, 4, 8],
                             help="Specifies the number of GPUs for tensor-parallelism "
                                  "during inference. (Only supported for Linux builds)")
        parser.add_argument("--pp-size", type=int, default=1, choices=[1, 2, 4, 8],
                            help="Specifies the number of GPUs for pipeline-parallelism "
                                 "during inference. (Only supported for Linux builds)")
        input_group.add_argument("--from-spec",
                            help=argparse.SUPPRESS)

        BuildSubcommand._add_common_onnx_and_llm_options(parser)

    @staticmethod
    def _add_request_id_build_options_to_parser(parser: argparse.ArgumentParser):
        parser.add_argument("request_id", help="""
            Request ID of a previously-started build.
            May only be provided if the build status has not already been reported as finished.
        """)
        BuildSubcommand._add_common_build_options(parser)


    @staticmethod
    def add_subparser(subparsers: argparse._SubParsersAction, subcommand_name: str) -> ArgumentParser:
        """
        Adds the 'build' subcommand to the main CLI argument parser.
        """
        build_subcommand = subparsers.add_parser(subcommand_name, help="Build a TRT engine on the cloud.")
        build_type = build_subcommand.add_subparsers(help="Types of builds", dest="build_type", required=True)
        onnx_subparser = build_type.add_parser(BuildType.ONNX.value,
                                               help="Build a TRT Engine from an onnx model.")
        BuildSubcommand._add_onnx_build_options_to_parser(onnx_subparser)

        trtllm_subparser = build_type.add_parser(BuildType.TRT_LLM.value,
                                                 help="Build a TRT-LLM Engine.")
        BuildSubcommand._add_trtllm_build_options_to_parser(trtllm_subparser)

        request_id_subparser = build_type.add_parser(BuildType.REQUEST_ID.value,
                                                     help="Resume an existing build from a request-id.")
        BuildSubcommand._add_request_id_build_options_to_parser(request_id_subparser)

        return build_subcommand

    def run(self, args):
        """
        Execute the 'build' subcommand with the given args.

        The 'build' subcommand is used to start a new engine build, or to resume
        a previously-started build.

        Raises ValueError if args are invalid.
        """
        trtcloud_client = TRTCloud()
        build_type = BuildType(args.build_type)

        output_file = args.out
        if build_type is BuildType.REQUEST_ID:
            trtcloud_client.continue_build(
                request_id=args.request_id,
                out_file=output_file
            )

        elif build_type in {BuildType.ONNX, BuildType.TRT_LLM}:
            tags = args.tags

            # OS and GPU can be specified either as args (eg. `--arg_name value`),
            # or as tags (eg. `--tag arg_name=value`);
            # Check if there are any conflicts,
            # and always move them to args to avoid having to check in both places
            for arg_name in ("os", "gpu"):
                arg_tag_idx = next(
                    (
                        tag_idx
                        for tag_idx, tag in enumerate(tags)
                        if tag.startswith(f"{arg_name}=")
                    ),
                    None,
                )
                # Compare the arg (--arg_name) and tag (--tag arg_name=) versions to ensure they match,
                # and always move the tag version to the args.
                if arg_tag_idx is not None:
                    arg_value = getattr(args, arg_name, None)
                    arg_tag_value = tags.pop(arg_tag_idx).split("=", 1)[1]

                    # Only tag is specified: move it to the args
                    if arg_value is None:
                        setattr(args, arg_name, arg_tag_value)

                    elif arg_value != arg_tag_value:
                        raise ValueError(
                            f"Conflicting parameters '--{arg_name}={arg_value}' and '--tag {arg_name}={arg_tag_value}'"
                        )

            # Validate args
            if bool(args.function_id) != bool(args.function_version):
                raise ValueError(
                    "Both args are required when either one is used: --function-id and --function-version"
                )

            if not args.os and not args.function_id and not args.function_version:
                raise ValueError("The following arg is required: --os")

            if not args.gpu and not args.function_id and not args.function_version:
                raise ValueError("The following arg is required: --gpu")

            if build_type is BuildType.TRT_LLM \
                and args.os.lower().strip() == "windows" \
                and (args.tp_size > 1 or args.pp_size > 1):
                raise ValueError("Tensor/Pipeline parallelism for inference is unsupported on Windows.")

            if args.local_refit and not args.strip_weights:
                raise ValueError("--local-refit is only applicable for builds with --strip-weights")

            if build_type is BuildType.ONNX:
                trtexec_args: List[str] = [arg for arg in (args.trtexec_args or "").split(" ") if arg]

                # Start a new ONNX build.
                trtcloud_client.start_onnx_build(
                    onnx_model=args.model,
                    gpu=args.gpu,
                    os_name=args.os,
                    trt_version=args.trt_version,
                    strip_weights=args.strip_weights,
                    local_refit=args.local_refit,
                    trtexec_args=trtexec_args,
                    out_file=output_file,
                    function_id=args.function_id,
                    function_version=args.function_version,
                    tags=tags
                )

            else:
                input_source = None
                if args.from_spec:
                    input_source = TRTLLMSpecSource(spec_path=args.from_spec)
                    check_and_display_huggingface_repo_engine_eulas(
                        [source["source"]["id"] for source in input_source.iter_input_sources(
                            input_type_filter="huggingface_repo")])
                elif args.hf_repo:
                    input_source = HFCheckpointSource(hf_repo=args.hf_repo,
                                                      hf_repo_revision=args.hf_repo_revision)
                    check_and_display_huggingface_repo_engine_eulas([args.hf_repo])
                elif args.trtllm_checkpoint:
                    input_source = TRTLLMCheckpointSource(url_or_filepath=args.trtllm_checkpoint)

                if not isinstance(input_source, TRTLLMSpecSource):
                    kv_quantization_type = None
                    if args.quantize_kv_cache:
                        is_input_model_gemma =  (isinstance(input_source, HFCheckpointSource) and
                                                 ModelLicenseFamily.GEMMA.value in input_source.hf_repo)

                        if not args.quantization:
                            raise ValueError("A quantization type (--quantization) is"
                                             " required when using --quantize-kv-cache.")
                        if args.quantization is TRTLLMQuantizationType.INT4_AWQ:
                            kv_quantization_type = TRTLLMKVQuantizationType.INT8
                        elif args.quantization is TRTLLMQuantizationType.FP8:
                            kv_quantization_type = TRTLLMKVQuantizationType.FP8
                        elif args.quantization is TRTLLMQuantizationType.FULL_PREC and is_input_model_gemma:
                            kv_quantization_type = TRTLLMKVQuantizationType.FP8
                        else:
                            raise ValueError(f"--quantize-kv-cache is unsupported for the input"
                                             f" model and quantization type {args.quantization.value}")

                    if kv_quantization_type is not None:
                        logging.info(f"Will use KV quantization type: {kv_quantization_type.value}. "
                                     f"Please Note: fp8 requires SM89 or higher, and is not supported on all GPUs.")

                    trtllm_recipe = TRTLLMRecipe(
                        data_type=args.dtype,
                        quantization_type=args.quantization,
                        kv_quantization_type=kv_quantization_type,
                        max_input_len=args.max_input_len,
                        max_seq_len=args.max_seq_len,
                        max_batch_size=args.max_batch_size,
                        max_num_tokens=args.max_num_tokens,
                        tp_size=args.tp_size,
                        pp_size=args.pp_size,
                        trtllm_version=args.trtllm_version,
                    )
                else:
                    trtllm_recipe = None

                tokenizer_source = None
                if not isinstance(input_source, TRTLLMCheckpointSource) and args.tokenizer:
                    raise ValueError("Tokenizers are only supported with builds from a TRT-LLM Checkpoint.")
                elif args.tokenizer:
                    tokenizer_source = TokenizerSource(url_or_filepath=args.tokenizer)

                trtcloud_client.start_trtllm_build(
                    gpu=args.gpu,
                    os_name=args.os,
                    strip_weights=args.strip_weights,
                    local_refit=args.local_refit,
                    build_input_source=input_source,
                    tokenizer_input_source=tokenizer_source,
                    trtllm_build_recipe=trtllm_recipe,
                    build_return_type=args.return_type,
                    out_file=output_file,
                    function_id=args.function_id,
                    function_version=args.function_version,
                    tags=tags
                )
        else:
            raise NotImplementedError()
