# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import enum
import os
import zipfile
from functools import lru_cache
from pathlib import Path
from typing import Iterable

import requests
from rich.progress import (BarColumn, DownloadColumn, Progress,
                           TaskProgressColumn, TextColumn, TimeRemainingColumn)

from trt_cloud.constants import (COMMON_ENGINE_LICENSE_TEXT,
                                 TRTC_PREBUILT_ENGINE_ORG,
                                 TRTC_PREBUILT_ENGINE_TEAM)


def download_file(
    url: str,
    output_filepath: str,
    headers: dict = None,
    quiet: bool = False
) -> str:
    response = requests.get(url, allow_redirects=True, stream=True, headers=headers)
    if not response.ok:
        raise RuntimeError(f"Failed to download {url}", response)

    total_length = int(response.headers["Content-Length"])
    chunk_size = 2 ** 20  # 1MB

    # Create a Progress bar
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        disable=quiet,
    ) as progress:

        # Create a Task object to represent the progress of the download
        task = progress.add_task(f"Downloading to {os.path.basename(output_filepath)}", total=total_length)

        with open(output_filepath, "wb") as output:
            for content in response.iter_content(chunk_size):
                if content:
                    output.write(content)
                    progress.update(task, advance=len(content))

    return output_filepath


def check_and_display_eula(license_path: str, eula_name: str, license_preamble: str = "",
                           license_path_format_string="Please find a copy of the license here: {}.") -> bool:
    if os.path.exists(license_path):
        with open(license_path, "r", encoding="utf8") as f:
            license_text = f.read()
    else:
        raise ValueError(f"{eula_name} not found. Must agree to EULA to proceed.")
    print(f"\n{eula_name}\n{license_preamble}{license_text}"
          f"\n{license_path_format_string.format(license_path)}\n")
    user_input = input(
        f"Do you agree to the {eula_name}? (yes/no) "
    ).lower().strip()

    user_agreed = user_input in {"y", "yes"}
    if not user_agreed:
        raise ValueError(f"You must agree to the {eula_name} to proceed.")

    return user_agreed

class ModelLicenseFamily(str, enum.Enum):
    LLAMA = "llama"
    PHI = "phi"
    GEMMA = "gemma"
    MISTRAL = "mistral"

def _get_license_type_from_repo_id(repo_id: str):
    for model_family in ModelLicenseFamily:
        if model_family.value in repo_id:
            return model_family.value
    raise ValueError(
        f"Huggingface repo {repo_id} is unsupported."
    )


def check_and_display_huggingface_repo_engine_eulas(repo_ids: Iterable[str]):
    for repo_id in repo_ids:
        model_license_family = _get_license_type_from_repo_id(repo_id)
        license_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "model_licenses",
                                    model_license_family,
                                    "ATTRIBUTION.txt")

        check_and_display_eula(license_path,f"EULA for use of huggingface repo: {repo_id}",
                               COMMON_ENGINE_LICENSE_TEXT,
                               "A copy will also be included in the engine archive.")


def upload_file(
    url: str,
    filepath: str,
    headers: dict = None,
):
    total_length = os.stat(filepath).st_size
    chunk_size = 2 ** 20  # 1MB

    class ReadFileWithProgressBar(object):
        def __init__(self, filepath):
            self.file = open(filepath, "rb")
            self.total_length = os.stat(filepath).st_size
            self.progress = Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                DownloadColumn(),
                TaskProgressColumn(),
                TimeRemainingColumn(),
            )
            self.progress.start()
            self.task = self.progress.add_task(f"Uploading {filepath}", total=self.total_length)

        def read(self, size=chunk_size):
            chunk = self.file.read(size)
            self.progress.update(self.task, advance=len(chunk))
            if len(chunk) == 0:
                self.progress.stop()
            return chunk

        def __len__(self):
            return total_length

    resp = requests.put(
        url,
        data=ReadFileWithProgressBar(filepath),
        headers=headers,
    )
    return resp

def extract_onnx_file(tmpdir, onnx_zip) -> str:
    with zipfile.ZipFile(onnx_zip, "r") as zip:
        zip.extractall(tmpdir)
    onnx_files_in_zip = list(Path(tmpdir).rglob('*.onnx'))
    if not onnx_files_in_zip:
        raise ValueError(f"No .onnx files found in {onnx_zip}.")
    if len(onnx_files_in_zip) > 1:
        raise ValueError(
            f"Multiple .onnx files found in archive: {onnx_files_in_zip}"
        )
    return str(onnx_files_in_zip[0])


def add_verbose_flag_to_parser(parser):
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase logging verbosity.")


@lru_cache()
def get_ngc_model_org():
    return os.environ.get("TRTC_ENGINE_ORG", "") or TRTC_PREBUILT_ENGINE_ORG


@lru_cache()
def get_ngc_model_team():
    return os.environ.get("TRTC_ENGINE_TEAM", None) or TRTC_PREBUILT_ENGINE_TEAM
