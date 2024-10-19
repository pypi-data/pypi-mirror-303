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
This file maps TRT versions and GPUs to NVCF functions.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Set

from trt_cloud.constants import TRTC_NCAID


@dataclass
class BuilderFunction:
    func_id: str
    version_id: str
    gpu: str
    os: str
    created_at: datetime
    is_latest: bool
    trt_versions: List[str] = field(default_factory=list)
    trtllm_versions: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)


def parse_versions_from_functions(fns: List[Dict]) -> List[BuilderFunction]:
    # Filter for active functions with the correct NCA ID
    fns = filter(
        lambda fn: fn["ncaId"] == TRTC_NCAID
        and fn["status"] == "ACTIVE"
        and fn["name"].startswith("trtc_builder"),
        fns,
    )
    fns = sorted(fns, key=lambda fn: fn["createdAt"], reverse=True)
    tags_combos: Set[str] = (
        set()
    )  # set of unique function tag combinations (incl. OS and GPU)
    ret = list()

    for fn in fns:
        # Sort tags in alphabetical order to ensure consistent ordering in `tags_combos`
        tags = sorted(
            [
                # Parse a double underscore '__' as an equals sign '=', since NVCF doesn't support '='
                # Eg. `os__linux` becomes `os=linux`
                tag.replace("__", "=", 1)
                for tag in (fn.get("tags") or [])
                # Hide tags that start with '_' as they are internal
                if not tag.startswith("_")
            ]
        )

        # Parse the os, gpu, TRT Versions, and TRT-LLM Versions from function tags
        os = gpu = None
        trt_versions = None
        trtllm_versions = ["0.11.0"]
        for tag in tags:
            if tag.startswith("os=") and len(tag) > 3:
                os = tag[3:]
            if tag.startswith("gpu=") and len(tag) > 4:
                gpu = tag[4:]
            if tag.startswith("trt_versions="):
                trt_versions = [
                    trt_version.replace("-", ".")
                    for trt_version in tag[len("trt_versions="):].split("_")
                ]
            for tagname in ["trtllm_version=", "trtllm_versions="]:
                if tag.startswith(tagname):
                    trtllm_versions = [
                        trt_version.replace("-", ".")
                        for trt_version in tag[len(tagname):].split("_")
                    ]

        # Skip functions without the required tags
        if not os or not gpu:
            continue

        # Check if a newer version for this combination of tags (incl. GPU and OS) already exists.
        # If so still add them so we can select it by id/version, but the version will be hidden
        # by default, and not selectable by os/gpu/tags.
        tags_str = ",".join(tags)
        is_latest = tags_str not in tags_combos
        if is_latest:
            tags_combos.add(tags_str)

        # Remove trailing 'Z' which python versions <3.11 don't support
        if fn["createdAt"].endswith("Z"):
            fn["createdAt"] = f"{fn['createdAt'][:-1]}+00:00"
        created_at = datetime.fromisoformat(fn["createdAt"])

        ret.append(
            BuilderFunction(
                func_id=fn["id"],
                version_id=fn["versionId"],
                gpu=gpu,
                os=os,
                tags=tags,
                created_at=created_at,
                trt_versions=trt_versions,
                trtllm_versions=trtllm_versions,
                is_latest=is_latest,
            )
        )
    return ret
