# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import json
import os.path
from abc import ABC, abstractmethod
from typing import Dict, Iterable, Iterator, List, Optional, Set


def _check_file_path(file_path: str, allowed_extensions: Iterable[str] = None):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not exist, or is not a file.")

    if allowed_extensions is not None:
        _, file_ext = os.path.splitext(os.path.basename(file_path))

        if file_ext not in allowed_extensions:
            raise ValueError(f"Unsupported file format {file_ext}")


def _is_path_url(path) -> bool:
    return (path.startswith("https://") or path.startswith("http://"))


class BuildInputSource(ABC):
    @abstractmethod
    def get_input_spec(self) -> dict: ...


class HFCheckpointSource(BuildInputSource):
    def __init__(self, hf_repo: str, hf_repo_revision: Optional[str] = None):
        self.hf_repo = hf_repo
        self.hf_repo_revision = hf_repo_revision

    def get_input_spec(self) -> dict:
        input_spec = {
            "type": "huggingface_checkpoint",
            "source": {
                "source_type": "huggingface_repo",
                "id": self.hf_repo,
            }
        }
        if self.hf_repo_revision is not None:
            input_spec["source"]["revision"] = self.hf_repo_revision

        return input_spec


class FileOrUrlBuildInputSource(BuildInputSource, ABC):
    def __init__(self, url_or_filepath: str):
        self.url_or_filepath = None
        self.is_url = False
        self.nvcf_asset_ids = []
        self.init_path(url_or_filepath)

    def init_path(self, path: str):
        self.url_or_filepath = path
        self.is_url = _is_path_url(self.url_or_filepath)
        if not self.is_url:
            _check_file_path(
                file_path=self.url_or_filepath,
                allowed_extensions=self.get_allowed_file_extensions()
            )

    def set_nvcf_asset_ids(self, nvcf_asset_ids: Iterable[str]):
        self.nvcf_asset_ids = nvcf_asset_ids

    def get_input_spec(self) -> dict:
        if self.is_url:
            return {
                "type": self.get_api_file_type(),
                "source": {
                    "source_type": "url",
                    "url": self.url_or_filepath
                }
            }
        else:
            if not self.nvcf_asset_ids:
                raise ValueError("No nvcf asset ids provided for local filepath.")

            return {
                "type": self.get_api_file_type(),
                "source": {
                    "source_type": "nvcf_asset",
                    "asset_id": list(self.nvcf_asset_ids)
                }
            }

    @abstractmethod
    def get_api_file_type(self) -> str: ...

    @abstractmethod
    def get_allowed_file_extensions(self) -> Set[str]: ...


class TRTLLMCheckpointSource(FileOrUrlBuildInputSource):
    def get_api_file_type(self) -> str:
        return "trtllm_checkpoint"

    def get_allowed_file_extensions(self) -> Set[str]:
        return {".zip"}


class TokenizerSource(FileOrUrlBuildInputSource):
    def get_api_file_type(self) -> str:
        return "tokenizer"

    def get_allowed_file_extensions(self) -> Set[str]:
        return {".json", ".model", ".zip"}


class ONNXModelSource(FileOrUrlBuildInputSource):
    def get_api_file_type(self) -> str:
        return "onnx"

    def get_allowed_file_extensions(self) -> Set[str]:
        return {".zip", ".onnx"}


class TRTLLMSpecSource:
    def __init__(self, spec_path: str):
        if _is_path_url(spec_path):
            raise ValueError("TRT LLM spec must be a local path and not a URL.")

        self.spec_path = spec_path
        _check_file_path(file_path=self.spec_path, allowed_extensions={".json"})
        self._raw_input_spec = self._get_raw_input_spec()

    def _get_raw_input_spec(self) -> dict:
        with open(self.spec_path) as spec_fhandle:
            return json.load(spec_fhandle)

    def iter_input_sources(self, input_type_filter: Optional[str] = None) -> Iterator[dict]:
        inputs = self._raw_input_spec.get("inputs", [])
        for build_input in inputs:
            source = build_input.get("source", None)
            if source is None:
                raise ValueError(f"Input {input} has no source.")

            if input_type_filter and build_input["source"]["source_type"] != input_type_filter:
                continue

            yield build_input

    def get_local_paths(self) -> List[str]:
        candidate_local_paths = []
        for build_input in self.iter_input_sources(input_type_filter="local_file"):
            input_source = build_input["source"]
            local_file_path = input_source["path"]
            _check_file_path(file_path=local_file_path)
            candidate_local_paths.append(local_file_path)

        return candidate_local_paths

    def set_local_path_nvcf_asset_ids(self, path_nvcf_ids: Dict[str, List[str]]):
        updated_input_sources = []
        for build_input in self.iter_input_sources():
            input_source = build_input["source"]

            if input_source["source_type"] == "local_file":
                local_file_path = input_source["path"]

                if local_file_path not in path_nvcf_ids:
                    raise ValueError(f"No nvcf_asset_ids provided for file {local_file_path}")

                updated_input_sources.append(
                    {
                        "type": build_input["type"],
                        "source": {
                            "source_type": "nvcf_asset",
                            "asset_id": path_nvcf_ids[local_file_path]
                        }
                    }
                )
            else:
                updated_input_sources.append(build_input)

        self._raw_input_spec["inputs"] = updated_input_sources

    def get_input_spec(self) -> dict:
        return self._raw_input_spec
