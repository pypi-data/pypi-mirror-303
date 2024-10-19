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
TRT Cloud CLI constants.
"""

import os

LICENSE_PATH = os.path.join(os.path.dirname(__file__), 'LICENSE.txt')
ENGINE_LICENSE_PATH = os.path.join(os.path.dirname(__file__), 'ENGINE_LICENSE.txt')
TRTC_PREBUILT_ENGINE_LICENSE_URL = ("https://docs.nvidia.com/deeplearning/tensorrt-cloud/"
                                    "latest/reference/eula.html#nvidia-tensorrt-engine-license-agreement")
COMMON_ENGINE_LICENSE_TEXT = ("GOVERNING TERMS: The use of this TensorRT Engine "
                              f"is governed by the NVIDIA TRT Engine License: {TRTC_PREBUILT_ENGINE_LICENSE_URL} \n\n")
COMMON_ENGINE_LICENSE_SUFFIX = ("A temporary copy of this document can be found at: {}\n"
                                "This will be deleted after a response to this prompt. "
                                "A copy is also included with the downloaded engine archive.")


TRTC_NCAID = "2gRA8clykzsMIoa9SG2xtooehNeUBk-CRIrWbbCnkyQ"
TRTC_PREBUILT_NVIDIA_ORG_NAME = "nvidia"
TRTC_PREBUILT_ENGINE_ORG = "nvidia"
TRTC_PREBUILT_ENGINE_TEAM = None
TRTC_PREBUILT_COLLECTION_NAME = "trt_cloud_prebuilt_engines"

TENSORRT_LIBS_PACKAGE_NAME = "tensorrt-cu12-libs"

MESSAGE_SUGGESTIONS = {
    "oom": (
        "It is likely that the selected GPU does not have enough memory to build the selected model. "
        "Please try again with a GPU with more memory."
    )
}

BUILD_SUGGESTIONS = {
    "CUDA out of memory": MESSAGE_SUGGESTIONS["oom"],
    "Cannot copy out of meta tensor": MESSAGE_SUGGESTIONS["oom"]
}
