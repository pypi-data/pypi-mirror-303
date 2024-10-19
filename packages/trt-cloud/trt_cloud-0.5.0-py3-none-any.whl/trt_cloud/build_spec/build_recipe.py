# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

from abc import ABC, abstractmethod
from typing import List, Optional

from trt_cloud.build_spec.build_options import (TRTLLMDtype,
                                                TRTLLMKVQuantizationType,
                                                TRTLLMQuantizationType)


class BuildRecipeBase(ABC):
    @abstractmethod
    def get_recipe_spec(self) -> dict: ...


class TrtexecArgListRecipe(BuildRecipeBase):
    RECIPE_NAME = "trtexec_arg_list"

    def __init__(self,
                 trt_version: Optional[str] = None,
                 trtexec_args: Optional[List[str]] = None):
        self.trt_version = trt_version
        self.trtexec_args = trtexec_args

    def get_recipe_spec(self) -> dict:
        ret = {
            "recipe_name": self.RECIPE_NAME,
        }
        if self.trt_version:
            ret["trt_version"] = self.trt_version
        if self.trtexec_args:
            ret["trtexec_args"] = self.trtexec_args
        return ret


class TRTLLMRecipe(BuildRecipeBase):
    RECIPE_NAME = "trtllm_trtcloud"

    def __init__(self,
                 data_type: Optional[TRTLLMDtype] = None,
                 quantization_type: TRTLLMQuantizationType = TRTLLMQuantizationType.FULL_PREC,
                 kv_quantization_type: Optional[TRTLLMKVQuantizationType] = None,
                 strip_plan: bool = False,
                 max_input_len: Optional[int] = None,
                 max_seq_len: Optional[int] = None,
                 max_batch_size: Optional[int] = None,
                 max_num_tokens: Optional[int] = None,
                 tp_size: Optional[int] = None,
                 pp_size: Optional[int] = None,
                 trtllm_version: Optional[str] = None):

        self.dtype = data_type
        self.quantization_type = quantization_type
        self.kv_quantization_type = kv_quantization_type
        self.strip_plan = strip_plan
        self.max_input_len = max_input_len
        self.max_seq_len = max_seq_len
        self.max_batch_size = max_batch_size
        self.max_num_tokens = max_num_tokens
        self.tp_size = tp_size
        self.pp_size = pp_size
        self.trtllm_version = trtllm_version

    def _get_multidevice_spec(self) -> dict:
        return {
            "tp_size": self.tp_size if self.tp_size is not None else 1,
            "pp_size": self.pp_size if self.pp_size is not None else 1
        }

    def _get_quantization_spec(self) -> dict:
        spec = {"qformat": self.quantization_type.value}
        if self.kv_quantization_type is not None:
            spec["kv_cache_dtype"] = self.kv_quantization_type.value

        return spec

    def set_trtllm_version(self, trtllm_version: str):
        self.trtllm_version = trtllm_version

    def get_recipe_spec(self) -> dict:
        ret = {
            "recipe_name": self.RECIPE_NAME,
            "trtllm_version": self.trtllm_version,
            "quantization": self._get_quantization_spec(),
            "strip_plan": self.strip_plan,
            "multidevice": self._get_multidevice_spec(),
        }

        if self.dtype:
            ret["dtype"] = self.dtype.value

        for field, val in {"max_input_len": self.max_input_len,
                           "max_seq_len": self.max_seq_len,
                           "max_batch_size": self.max_batch_size,
                           "max_num_tokens": self.max_num_tokens}.items():
            if val is not None:
                ret[field] = val

        return ret
