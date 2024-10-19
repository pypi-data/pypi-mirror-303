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
Manage state for the TRT Cloud CLI which is preserved between uses.

Currently this includes a config file with login credentials and a NVCF asset cache.
"""

import configparser
import dataclasses
import datetime
import hashlib
import importlib.metadata
import json
import logging
import os
import platform
import shutil
from typing import Dict, Tuple

# Directory where TRT Cloud stores persistent state.
TRT_CLOUD_DIR = {
    "Linux": os.path.join(os.path.expanduser("~"), ".trt-cloud"),
    "Darwin": os.path.join(os.path.expanduser("~"), ".trt-cloud"),
    "Windows": os.path.join(os.path.expandvars("%appdata%"), "NVIDIA", "TRT Cloud"),
}[platform.system()]

CONFIG_FILE = os.path.join(TRT_CLOUD_DIR, "config")
CONFIG_FILE_BACKUP = os.path.join(TRT_CLOUD_DIR, "config.backup")
ASSET_CACHE_FILE = os.path.join(TRT_CLOUD_DIR, "nvcf_asset_cache.json")

# List of files created by TRT Cloud to store persistent state.
ALL_STATE_FILES = [
    CONFIG_FILE,
    CONFIG_FILE_BACKUP,
    ASSET_CACHE_FILE
]

def _add_state_files_to_package_records():
    """
    Tell pip that when uninstalling TRT Cloud, it should also delete
    the files in the list ALL_STATE_FILES.
    """

    # Find the RECORDS file in site-packages/trt_cloud-*.dist-info/
    # This file tells pip which files to remove when uninstalling TRT Cloud.
    dist_files = importlib.metadata.files("trt_cloud")
    for file in dist_files:
        record_file = str(file.locate())
        if os.path.split(record_file)[-1] == "RECORD":
            break
    else:
        logging.warning(
            "Cannot find RECORD file in package installation. "
            "The TRT Cloud directory (~/.trt-cloud) will NOT be removed "
            "if TRT Cloud is uninstalled with pip."
        )
        return

    with open(record_file, "a", encoding="utf-8") as f:
        for state_file in ALL_STATE_FILES:
            f.write(state_file)

            # Commas for empty hash value.
            f.write(",,\n")

def _create_trt_cloud_dir():
    """ Create a directory for storing TRT Cloud state. """
    os.makedirs(TRT_CLOUD_DIR, exist_ok=True)

class TRTCloudConfig:
    """
    Class for managing persistent user config for TRT Cloud.
    """

    def __init__(self):
        _create_trt_cloud_dir()

        # Create config if it doesn't already exist.
        if not os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'x'):
                pass

        if not self.is_package_records_modified():
            _add_state_files_to_package_records()
            self.set_package_records_modified()

    def read_saved_login(self) -> Tuple[str, str, str]:
        """
        Read login credentials from the config file.
        """
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if 'login' not in config:
            return None, None, None
        login_config = config['login']

        return (
            login_config.get('client_id'),
            login_config.get('client_secret'),
            login_config.get('nvapi_key'),
        )

    def save_login(
        self,
        client_id: str = None,
        client_secret: str = None,
        nvapi_key: str = None
    ):
        """
        Write login credentials to the config file.
        NOTE: credentials are stored in plaintext.
        """
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        # Clear old login config.
        config['login'] = {}

        if client_id:
            config['login']['client_id'] = client_id
        if client_secret:
            config['login']['client_secret'] = client_secret
        if nvapi_key:
            config['login']['nvapi_key'] = nvapi_key

        with open(CONFIG_FILE, 'w') as f:
            config.write(f)

    def backup(self):
        """Back up the config file."""
        shutil.copy(CONFIG_FILE, CONFIG_FILE_BACKUP)

    def restore_backup(self):
        """Restore the config file backup."""
        shutil.copy(CONFIG_FILE_BACKUP, CONFIG_FILE)

    def agreed_to_license(self, version: str) -> bool:
        """Return whether the user has agreed to the TRT Cloud license."""
        return bool(self._read_config("license", version))

    def save_agreed_to_license(self, version: str):
        """Agree to the TRT Cloud license."""
        self._write_config("license", version, "True")

    def agreed_to_engine_license(self, version: str) -> bool:
        """Return whether the user has agreed to the TRT Cloud Prebuilt Engine license."""
        return bool(self._read_config("prebuilt_license", version))

    def save_agreed_to_engine_license(self, version: str):
        """Agree to the TRT Cloud Prebuilt Engine license."""
        self._write_config("prebuilt_license", version, "True")

    def is_package_records_modified(self):
        return self._read_config("install", "records_modified")

    def set_package_records_modified(self):
        self._write_config("install", "records_modified", "True")

    def unlock_all_commands(self):
        self._write_config("unlock", "ga", "True")

    def are_all_commands_unlocked(self) -> bool:
        return self._read_config("unlock", "ga")

    def _read_config(self, parent: str, child: str) -> str:
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if parent not in config:
            return None

        return config[parent].get(child)

    def _write_config(self, parent: str, child: str, value: str):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        if parent not in config:
            config[parent] = {}
        config[parent][child] = value

        with open(CONFIG_FILE, 'w') as f:
            config.write(f)

@dataclasses.dataclass
class AssetCacheEntry:
    nvcf_asset_id: str
    expires_at: datetime.datetime

class NVCFAssetCache:
    """
    Class for reading and writing the NVCF asset cache.
    The cache is helpful to prevent uploading the same input file multiple times.

    The cache file has the following JSON format:

    {
        "<file_hash>": {
            "nvcf_asset_id": <str>,
            "expires_at": <datetime>
        },
        ...
    },
    """
    # How long NVCF keeps uploaded assets.
    NVCF_TTL = datetime.timedelta(days=1)

    # How long before the upload expiration we should upload a new file anyway.
    TTL_BUFFER = datetime.timedelta(hours=2)

    def __init__(self):
        _create_trt_cloud_dir()

        # Create cache file if it doesn't already exist.
        if not os.path.exists(ASSET_CACHE_FILE):
            self.clear()

    def filehash(self, filepath: str) -> str:
        """
        Compute the SHA256 hash of a file.
        """
        block_size = 64 * 1024
        sha = hashlib.sha256()
        with open(filepath, "rb") as f:
            blob = f.read(block_size)
            while blob:
                sha.update(blob)
                blob = f.read(block_size)
        return sha.hexdigest()

    def create_new_entry(self, nvcf_asset_id) -> AssetCacheEntry:
        return AssetCacheEntry(
            nvcf_asset_id=nvcf_asset_id,
            expires_at=datetime.datetime.utcnow() + self.NVCF_TTL - self.TTL_BUFFER
        )

    def read(self) -> Dict[str, AssetCacheEntry]:
        with open(ASSET_CACHE_FILE, 'r') as f:
            cache_json = json.load(f)
        cache = {
            file_hash: AssetCacheEntry(
                nvcf_asset_id=entry["nvcf_asset_id"],
                expires_at=datetime.datetime.fromisoformat(entry["expires_at"]),
            )
            for file_hash, entry in cache_json.items()
        }
        return self._purge(cache)

    def _purge(self, cache):
        # Remove expired entries
        now = datetime.datetime.utcnow()
        return {
            filehash: entry
            for filehash, entry in cache.items()
            if entry.expires_at > now
        }

    def write(self, cache: Dict[str, AssetCacheEntry]):
        def _serialize_datetime(obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            raise TypeError

        cache = self._purge(cache)
        cache_json = {
            file_hash: dataclasses.asdict(entry)
            for file_hash, entry in cache.items()
        }
        with open(ASSET_CACHE_FILE, 'w') as f:
            json.dump(cache_json, f, indent=4, default=_serialize_datetime)

    def clear(self):
        self.write({})
