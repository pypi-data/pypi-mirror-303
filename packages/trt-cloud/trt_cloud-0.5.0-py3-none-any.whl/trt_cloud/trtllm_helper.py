# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import os.path
from importlib import metadata

from packaging import version


class TRTLLMHelper:
    @classmethod
    def _validate_checkpoint_directory(cls, checkpoint_directory) -> None:
        if not os.path.exists(checkpoint_directory) or not os.path.isdir(checkpoint_directory):
            raise FileNotFoundError(f"{checkpoint_directory} does not exist, or is not a directory.")

    @classmethod
    def _can_prune_all(cls):
        required_version = version.parse("0.12.0")
        current_version = version.parse(metadata.version("tensorrt_llm"))
        return required_version <= current_version

    @classmethod
    def prune(cls, checkpoint_directory: str, output_directory: str):
        configs = {
            "ckpt_dir": os.path.abspath(checkpoint_directory),
            "out_dir": os.path.abspath(output_directory)
        }

        cls._validate_checkpoint_directory(checkpoint_directory)
        try:
            from tensorrt_llm.commands.prune import prune_and_save
            if cls._can_prune_all():
                configs["prune_all"] = True
            prune_and_save(**configs)
        except ImportError:
            raise RuntimeError("Failed to import tensorrt_llm, please make sure that TensorRT LLM is installed")
        except Exception:
            raise RuntimeError(f"Failed to prune LLM checkpoint in {checkpoint_directory}")
