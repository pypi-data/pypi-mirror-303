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
Module which contains NVCFClient, a client for NVCF.
"""

import logging
import os
import time
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import requests
from requests.auth import HTTPBasicAuth

from trt_cloud.utils import upload_file

NVCF_MAX_ASSET_SIZE = int(5e9) # 5GB
NVCF_POLL_SECONDS = 5 # seconds
DEFAULT_TIMEOUT = 120 # seconds
DEFAULT_NVCF_ENDPOINT = "https://api.nvcf.nvidia.com"
DEFAULT_AUTH_ENDPOINT = "https://tbyyhdy8-opimayg5nq78mx1wblbi8enaifkmlqrm8m.ssa.nvidia.com"
DEFAULT_SCOPES = ["invoke_function", "list_functions", "queue_details"]

class NVCFException(ValueError):
    """
    Class for raising an NVCF exception.
    """

    def __init__(self, message, response=None):
        err_str = message
        if response is not None:
            err_str += f"\n    Response status code: {response.status_code}"
            err_str += f"\n    Response text: {response.text}"
        super().__init__(err_str)

class SSA:
    """
    Class for using SSA to get an auth token.
    """
    def __init__(
        self,
        scopes: Optional[List[str]] = None,
        nvcf_endpoint: Optional[str] = None,
        auth_endpoint: Optional[str] = None,
        ssa_client_id: Optional[str] = None,
        ssa_client_secret: Optional[str] = None,
        nvapi_key: Optional[str] = None,
    ):
        self.nvcf_endpoint: str = nvcf_endpoint or DEFAULT_NVCF_ENDPOINT
        self.auth_endpoint: str = auth_endpoint or DEFAULT_AUTH_ENDPOINT
        self.scopes: List[str] = scopes if scopes is not None else DEFAULT_SCOPES

        self.ssa_client_id: Optional[str] = ssa_client_id
        self.ssa_client_secret: Optional[str] = ssa_client_secret
        self.nvapi_key: Optional[str] = nvapi_key

        self.nvcf_token: Optional[str] = None
        self.nvcf_token_expire: Optional[datetime] = None

    def get_token(self) -> str:
        """
        Generate an authentication token using SSA credentials.
        """

        if self.nvcf_token_expire and self.nvcf_token_expire > datetime.now() + timedelta(seconds=60):
            return self.nvcf_token

        auth_data = f"scope={'%20'.join(self.scopes)}&grant_type=client_credentials"

        resp = requests.post(
            url=f"{self.auth_endpoint}/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=HTTPBasicAuth(self.ssa_client_id, self.ssa_client_secret),
            data=auth_data,
            timeout=DEFAULT_TIMEOUT,
        )

        if resp.status_code != 200:
            raise NVCFException("Unable to authorize with provided SSA Credentials.", resp)

        self.nvcf_token = resp.json()["access_token"]
        self.nvcf_token_expire = datetime.fromtimestamp(time.time() + resp.json()["expires_in"] - 1)
        logging.debug("Token received! Expires at: %s", str(self.nvcf_token_expire))

        return self.nvcf_token


class NVCFClient:
    """
    Class for listing and invoking NVCF Functions.
    """

    def __init__(
        self,
        scopes: Optional[List[str]] = None,
        nvcf_endpoint: Optional[str] = None,
        auth_endpoint: Optional[str] = None,
        ssa_client_id: Optional[str] = None,
        ssa_client_secret: Optional[str] = None,
        nvapi_key: Optional[str] = None,
    ):
        if not ((ssa_client_id and ssa_client_id) or nvapi_key):
            raise ValueError("No NVCF credentials provided. Please run 'trt-cloud login' first.")

        self.nvcf_endpoint: str = nvcf_endpoint or DEFAULT_NVCF_ENDPOINT
        self.nvapi_key: Optional[str] = nvapi_key
        self.ssa = SSA(
            scopes=scopes,
            auth_endpoint=auth_endpoint,
            ssa_client_id=ssa_client_id,
            ssa_client_secret=ssa_client_secret
        )


    @property
    def auth_header(self) -> dict:
        """
        Returns the Authentication header needed to call NVCF.
        """
        token = self.nvapi_key or self.ssa.get_token()
        return {"Authorization": f"Bearer {token}"}


    def _check_bad_response_bad_credentials(self, resp):
        if resp.status_code == 401:
            if self.nvapi_key:
                raise NVCFException(
                    "Invalid nvapi key. Please run 'trt-cloud login' and provide valid credentials. ",
                    resp
                )
            else:
                raise NVCFException("Auth token rejected.", resp)


    def get_functions(self) -> List[Dict[str, Any]]:
        """
        Get all NVCF functions available to this user..
        """
        resp = requests.get(
            url=f"\n{self.nvcf_endpoint}/v2/nvcf/functions",
            headers=self.auth_header,
            timeout=DEFAULT_TIMEOUT,
        )
        self._check_bad_response_bad_credentials(resp)
        if resp.status_code != 200:
            raise NVCFException("Unable to list all NVIDIA Cloud Functions", resp)

        return resp.json()["functions"]


    def get_request_status(self, req_id: str) -> requests.Response:
        """
        Get details for the NVCF function invocation with the given request ID.
        Possible return status:
            200: The function invocation is complete. The response content has the return value
                 of the NVCF function.
            202: The function invocation is incomplete.
            302: The function invocation is complete. See the "Location" header in the response for
                 the download URL of the result.
            404: Unknown request ID. This will happen if get_request_status is called
                 after already having returned status 200 or 302.
        """
        headers = self.auth_header
        headers['NVCF-POLL-SECONDS'] = str(NVCF_POLL_SECONDS)

        resp = requests.get(
            url=f"{self.nvcf_endpoint}/v2/nvcf/pexec/status/{req_id}",
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
            allow_redirects=False,
        )
        self._check_bad_response_bad_credentials(resp)

        if resp.status_code == 404:
            raise NVCFException(
                "Unknown request ID. This may be because the request status has already previously "
                "been reported as completed, or because the request ID has expired."
            )

        return resp

    def get_request_position_in_queue(self, req_id: str) -> str:
        """
        Return the position of request_id in the NVCF function queue.
        The return value is either the number converted into a string,
        or "Unknown" if the position is unknown.
        """
        resp = requests.get(
            url=f"\n{self.nvcf_endpoint}/v2/nvcf/queues/{req_id}/position",
            headers=self.auth_header,
            timeout=DEFAULT_TIMEOUT,
        )
        if resp.status_code == 200:
            return str(resp.json()["positionInQueue"])

        return "Unknown"


    def call_function(
        self,
        function_id: str,
        version_id: str,
        request_body: dict,
        asset_refs: List[str]
    ) -> requests.Response:
        """
        Call a NVCF function.
        See get_request_status for a list of possible response status codes.
        """

        headers = self.auth_header
        if asset_refs:
            headers['NVCF-INPUT-ASSET-REFERENCES'] = ','.join(asset_refs)
        headers['NVCF-POLL-SECONDS'] = str(NVCF_POLL_SECONDS)

        resp = requests.post(
            url=f"{self.nvcf_endpoint}/v2/nvcf/pexec/functions/{function_id}/versions/{version_id}",
            headers=headers,
            json=request_body,
            timeout=DEFAULT_TIMEOUT,
            allow_redirects=False,
        )
        self._check_bad_response_bad_credentials(resp)

        return resp

    def upload_new_asset(self, filepath: str, description: str = None) -> str:
        """
        Upload an asset to NVCF.
        Returns the Asset ID of the created asset.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"{filepath} not found")

        content_type = "application/octet-stream"

        #
        # Step 1: Get upload URL by creating a new NVCF asset
        #
        headers = self.auth_header
        headers.update({"Content-Type": "application/json", "accept": "application/json"})
        description = description if description else os.path.basename(filepath)
        body = {
            "contentType": content_type,
            "description": description,
        }
        resp = requests.post(
            url=f"{self.nvcf_endpoint}/v2/nvcf/assets",
            headers=headers,
            json=body,
        )
        self._check_bad_response_bad_credentials(resp)
        if resp.status_code != 200:
            raise NVCFException("Failed to create new NVCF Asset.", resp)

        #
        # Step 2: Upload asset to URL
        #
        res_json = resp.json()
        upload_url = res_json["uploadUrl"]
        asset_id = res_json["assetId"]

        headers = {
            "Content-Type": content_type,
            "x-amz-meta-nvcf-asset-description": description,
        }
        resp = upload_file(upload_url, filepath, headers=headers)
        if resp.status_code != 200:
            raise NVCFException("Failed to upload asset: ", resp)

        return asset_id
