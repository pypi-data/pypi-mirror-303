# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import base64
import functools
import json
import logging
import os
import tempfile
from datetime import datetime, timedelta
from typing import Optional, Tuple
from urllib.parse import urljoin

import requests

from trt_cloud.constants import (COMMON_ENGINE_LICENSE_SUFFIX,
                                 COMMON_ENGINE_LICENSE_TEXT,
                                 TRTC_PREBUILT_NVIDIA_ORG_NAME)
from trt_cloud.utils import check_and_display_eula, download_file

DEFAULT_NGC_ENDPOINT = "https://api.ngc.nvidia.com"
DEFAULT_AUTH_ENDPOINT = "https://authn.nvidia.com/token"


class NGCException(Exception):
    """Class for raising an NGC exception."""

    def __init__(self, message, response=None):
        err_str = message
        if response is not None:
            err_str += f"\n    Response status code: {response.status_code}"
            err_str += f"\n    Response text: {response.text}"
        super().__init__(err_str)


class NGCRegistryClient:
    """Class for querying a NGC registry."""

    def __init__(
        self,
        ngc_endpoint: Optional[str] = None,
        auth_endpoint: Optional[str] = None,
        ngc_org: Optional[str] = None,
        ngc_team: Optional[str] = None,
    ):
        self.ngc_registry_endpoint: str = ngc_endpoint or DEFAULT_NGC_ENDPOINT
        self.auth_endpoint: str = auth_endpoint or DEFAULT_AUTH_ENDPOINT
        self.ngc_org: str = ngc_org
        self.ngc_team: str = ngc_team
        self.is_org_nvidia: bool = (self.ngc_org == TRTC_PREBUILT_NVIDIA_ORG_NAME)

        self._auth_token: Optional[str] = None
        self._auth_token_expire: Optional[datetime] = None

    def list_models_in_collection(self, collection_name: str):
        page_size = 1000
        query = {
            "page": 0,
            "pageSize": page_size,
        }

        if self.is_org_nvidia:
            if self.ngc_team is not None:
                path = f"/v2/collections/{self.ngc_org}/{self.ngc_team}/{collection_name}/artifacts/models"
            else:
                path = f"/v2/collections/{self.ngc_org}/{collection_name}/artifacts/models"
        elif self.ngc_team is None:
            path = f"/v2/org/{self.ngc_org}/collections/{collection_name}/artifacts/models"
        else:
            path = f"/v2/org/{self.ngc_org}/team/{self.ngc_team}/collections/{collection_name}/artifacts/models"

        headers = self._auth_header() if self.ngc_org else None

        def _get_page_of_model_results(page_index: int = 0):
            query_copy = query.copy()
            query_copy["page"] = page_index
            url = urljoin(self.ngc_registry_endpoint, path)
            response = requests.get(url, headers=headers, params={"q": json.dumps(query_copy)})

            if not response.ok:
                raise NGCException("Unable to query NGC model registry.", response)

            response_json = response.json()
            num_pages = response_json["paginationInfo"]["totalPages"]

            this_page_models = response_json["artifacts"]
            return this_page_models, num_pages

        models, pages = _get_page_of_model_results(page_index=0)

        for idx in range(1, pages):
            page_models, _ = _get_page_of_model_results(page_index=idx)
            models += page_models

        return [model["name"] for model in models]

    def _get_api_path_for_model(self, model_name: str) -> str:
        if self.is_org_nvidia:
            if self.ngc_team is not None:
                return f"/v2/models/{self.ngc_org}/{self.ngc_team}/models/{model_name}"
            else:
                return f"/v2/models/{self.ngc_org}/{model_name}"
        elif self.ngc_team is None:
            return f"/v2/org/{self.ngc_org}/models/{model_name}"
        else:
            return f"/v2/org/{self.ngc_org}/team/{self.ngc_team}/models/{model_name}"

    def get_versions_for_model(self, model_name: str) -> dict:
        api_path = f"{self._get_api_path_for_model(model_name)}/versions"
        url = urljoin(self.ngc_registry_endpoint, api_path)
        headers = self._auth_header() if self.ngc_org else None

        def _extract_all_model_attributes(model_metrics: list) -> dict:
            model_attributes = {}
            for table in model_metrics:
                model_attributes.update({entry["key"]: entry["value"] for entry in table["attributes"]})

            return model_attributes

        def _get_page_of_version_results(page_index=0) -> Tuple[dict, int]:
            this_page_versions = {}

            response = requests.get(url, headers=headers, params={"page-size": 100, "page-number": page_index})
            if not response.ok:
                raise NGCException("Unable to query NGC model registry.", response)

            response_json = response.json()
            for model_version in response_json["modelVersions"]:
                this_page_versions[model_version["versionId"]] = _extract_all_model_attributes(
                    model_version.get("customMetrics", []))
                this_page_versions[model_version["versionId"]]["download_size"] = (
                    model_version.get('totalSizeInBytes', "0 Bytes"))

            return this_page_versions, int(response_json["paginationInfo"]["totalPages"])

        model_versions, num_pages = _get_page_of_version_results(page_index=0)
        for idx in range(1, num_pages):
            page_results, _ = _get_page_of_version_results(page_index=idx)
            model_versions.update(page_results)

        return model_versions

    def download_model(
        self,
        model_name,
        model_version,
        output_path
    ):
        api_path = f"{self._get_api_path_for_model(model_name)}/versions/{model_version}"

        with tempfile.TemporaryDirectory() as tmpdir:
            license_path = f"{api_path}/files/ATTRIBUTION.txt"
            engine_license_path = os.path.join(tmpdir, f"{model_name}_{model_version}_ATTRIBUTION.txt")
            download_file(urljoin(self.ngc_registry_endpoint, license_path),
                          output_filepath=engine_license_path, headers=self._auth_header(),
                          quiet=True)
            check_and_display_eula(engine_license_path,
                                   f"EULA for Model: {model_name}, Engine: {model_version}",
                                   COMMON_ENGINE_LICENSE_TEXT, COMMON_ENGINE_LICENSE_SUFFIX)

        engine_path = f"{api_path}/files/engine.zip"
        url = urljoin(self.ngc_registry_endpoint, engine_path)

        logging.info(f"Saving engine to {output_path}")
        download_file(url, output_filepath=output_path, headers=self._auth_header())

    @functools.lru_cache()
    def _ngc_get_token(self):
        '''Use the api key set environment variable to generate auth token '''

        NGC_API_KEY = os.environ.get("NGC_API_KEY")
        if not NGC_API_KEY:
            raise ValueError("Please define the NGC_API_KEY environment variable.")

        scope = f'group/ngc:{self.ngc_org}'
        if self.ngc_team:
            scope = [scope, scope + f'/{self.ngc_team}']

        querystring = {"service": "ngc", "scope": scope}
        auth = '$oauthtoken:{0}'.format(NGC_API_KEY)
        headers = {
            'Authorization': 'Basic {}'.format(base64.b64encode(auth.encode('utf-8')).decode('utf-8')),
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
        }

        response = requests.get(self.auth_endpoint, headers=headers, params=querystring)
        if response.status_code != 200:
            raise Exception("HTTP Error %d: from '%s'" % (response.status_code, self.auth_endpoint))
        resp_json = response.json()
        self._auth_token = resp_json["token"]
        self._auth_token_expire = datetime.now() + timedelta(seconds = resp_json["expires_in"] - 1)
        return self._auth_token

    @functools.lru_cache()
    def _auth_header(self):
        if os.environ.get("NGC_API_KEY") is not None:
            return {"Authorization": f"Bearer {self._ngc_get_token()}"}
        else:
            return None
