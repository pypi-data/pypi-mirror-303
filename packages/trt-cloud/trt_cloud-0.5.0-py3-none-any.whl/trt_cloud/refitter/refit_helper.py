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
import logging
import os
import pathlib
import platform
import re
import zipfile
from contextlib import contextmanager
from dataclasses import dataclass
from importlib import metadata
from tempfile import TemporaryDirectory
from typing import IO, Union

from polygraphy.backend.trt import EngineFromBytes, SaveEngine

from trt_cloud import utils
from trt_cloud.build_spec.build_options import BuildType
from trt_cloud.constants import TENSORRT_LIBS_PACKAGE_NAME

try:
    os.environ['TLLM_LOG_LEVEL'] = 'ERROR'
    from tensorrt_llm.builder import EngineConfig
    from tensorrt_llm.commands.refit import refit as refit_llm
    from tensorrt_llm.models import MODEL_MAP
except Exception:
    pass


@dataclass
class TrtVersion:
    major: int
    minor: int
    patch: int

    def __repr__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __hash__(self):
        return hash((self.major, self.minor, self.patch))

    @classmethod
    def from_version_str(cls, version_str: str) -> 'TrtVersion':
        version_regex = re.compile(r"([0-9]+)[^\.]*\.([0-9]+)[^\.]*\.([0-9]+).*")
        version_components = version_regex.findall(version_str)

        if not version_components or not len(version_components[0]) == 3:
            raise ValueError("Failed to Parse TRT Version")

        return TrtVersion(
            major=int(version_components[0][0]),
            minor=int(version_components[0][1]),
            patch=int(version_components[0][2])
        )


TRT_LLM_VERSION_MAP = {
    TrtVersion(10, 0, 1): "0.10.0",
    TrtVersion(10, 1, 0): "0.11.0",
    TrtVersion(10, 3, 0): "0.12.0"
}


class RefitHelper:
    @classmethod
    def _validate_file_path(cls, file_path: str):
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            raise ValueError(f"Invalid path {file_path}")

    @classmethod
    def _check_file_ext(cls, file_path: str, expected_extension: str) -> bool:
        filename, file_ext = os.path.splitext(os.path.basename(file_path))
        return file_ext == expected_extension

    def _read_trt_engine_version(self, engine_file: IO[bytes]) -> TrtVersion:
        engine_metadata = engine_file.read(28)
        engine_file.seek(0)

        if not engine_metadata or len(engine_metadata) < 28:
            raise ValueError("Failed to read trt version from engine file")

        try:
            # Byte 27 has the last version digit.
            return TrtVersion(
                major=int(engine_metadata[24]),
                minor=int(engine_metadata[25]),
                patch=int(engine_metadata[26])
            )
        except Exception:
            raise ValueError("Failed to read trt version from engine file")

    def _import_trt_runtime(self, is_engine_vc: bool) -> Union['tensorrt_lean', 'tensort']:  # noqa
        if is_engine_vc:
            import tensorrt_lean as trt
        else:
            import tensorrt as trt

        return trt

    def _validate_tensorrt_import(self, engine_tensorrt_version: TrtVersion, is_engine_vc: bool):
        tensorrt_python_package_name = "tensorrt-lean" if is_engine_vc else "tensorrt"

        try:
            trt = self._import_trt_runtime(is_engine_vc)
            try:
                installed_trt_version = TrtVersion.from_version_str(trt.__version__)
            except Exception:
                logging.warning(f"Failed to determine currently installed {tensorrt_python_package_name} version."
                                " Will attempt to continue. If you run into errors,"
                                f" please install {tensorrt_python_package_name} version {engine_tensorrt_version},"
                                f" or another compatible version.")
                return

            if installed_trt_version != engine_tensorrt_version:
                logging.warning(
                    f"Currently installed {tensorrt_python_package_name} version {installed_trt_version}"
                    f" is not the same as the version"
                    f" the engine was built with ({engine_tensorrt_version})."
                    f" Will attempt to continue. If you run into"
                    f" errors, please install {tensorrt_python_package_name} {engine_tensorrt_version}"
                    f" or another compatible version."
                )

        except ImportError:
            raise RuntimeError(
                f"Unable to import {tensorrt_python_package_name}. "
                f"To be able to refit the engine, please install {tensorrt_python_package_name}"
                f" version {engine_tensorrt_version}"
            )

    def _load_engine(self, engine_path: str, is_engine_vc: bool) -> 'tensorrt.ICudaEngine':  # noqa
        self._validate_file_path(engine_path)
        if self._check_file_ext(engine_path, ".zip"):
            with zipfile.ZipFile(engine_path) as build_result_zip:
                if "build_result/engine.trt" not in build_result_zip.namelist():
                    raise ValueError(f"{engine_path} does not contain a TRT engine (build_result/engine.trt)")

                with build_result_zip.open("build_result/engine.trt") as trt_engine:
                    try:
                        engine_trt_version = self._read_trt_engine_version(trt_engine)
                    except Exception:
                        raise RuntimeError(f"Failed to read TRT version from engine: {engine_path}")

                    self._validate_tensorrt_import(engine_trt_version, is_engine_vc)
                    return EngineFromBytes(trt_engine.read())()

        if self._check_file_ext(engine_path, ".trt"):
            with open(engine_path, "rb") as trt_engine:
                try:
                    engine_trt_version = self._read_trt_engine_version(trt_engine)
                except Exception:
                    raise RuntimeError(f"Failed to read TRT version from engine: {engine_path}")

                self._validate_tensorrt_import(engine_trt_version, is_engine_vc)
                return EngineFromBytes(serialized_engine=trt_engine.read())()
        else:
            raise ValueError(f"Unsupported engine input {engine_path}. Only build_result archives (.zip),"
                             f" and engine files (.trt) are supported.")

    def _refit_engine(self, trt_engine: 'tensorrt.ICudaEngine',  # noqa
                      onnx_model_path: str, is_engine_vc: bool) -> 'tensorrt.ICudaEngine':  # noqa
        self._validate_file_path(onnx_model_path)
        with TemporaryDirectory() as tmpdir:
            if self._check_file_ext(onnx_model_path, ".onnx"):
                refit_input_onnx = onnx_model_path
            elif self._check_file_ext(onnx_model_path, ".zip"):
                refit_input_onnx = utils.extract_onnx_file(tmpdir, onnx_model_path)
            else:
                raise ValueError(f"{onnx_model_path} does not appear to be a .onnx or a .zip file.")

            trt = self._import_trt_runtime(is_engine_vc)
            trt_logger = trt.Logger()
            trt_refitter = trt.Refitter(trt_engine, trt_logger)
            onnx_refitter = trt.OnnxParserRefitter(trt_refitter, trt_logger)
            if not onnx_refitter.refit_from_file(refit_input_onnx):
                raise RuntimeError(f"Failed to refit from model {onnx_model_path}")
            if not trt_refitter.refit_cuda_engine():
                raise RuntimeError("Failed to refit cuda engine")

        return trt_engine

    def _save_refitted_engine(self, refitted_engine: 'tensorrt.ICudaEngine', output_path: str):  # noqa
        dir_tree = os.path.dirname(os.path.abspath(output_path))
        if not os.path.exists(dir_tree):
            logging.info(f"Creating {dir_tree}")
            os.makedirs(dir_tree, exist_ok=True)

        SaveEngine(refitted_engine, output_path)()
        logging.info(f"Refitted engine saved to {output_path}")

    @contextmanager
    def _handle_llm_refit_input(self, input_name: str, input_path: str):
        with TemporaryDirectory() as extract_dir:
            if os.path.isdir(input_path):
                logging.info(f"Interpreting {input_path} as a {input_name} directory.")
                yield input_path
            else:
                _, file_ext = os.path.splitext(os.path.basename(input_path))
                if file_ext != ".zip":
                    raise ValueError(f"Unsupported {input_name} file extension {file_ext}")
                else:
                    logging.info(f"Interpreting {input_path} as {input_name} archive.")
                    logging.info(f"Extracting {input_name} from {input_path} -> {extract_dir}")
                    with zipfile.ZipFile(input_path) as input_zip:
                        input_zip.extractall(extract_dir)
                        if input_name == "engine":
                            yield os.path.join(extract_dir, "build_result", "engines")
                        else:
                            yield extract_dir

    def _check_trtllm_refit_version_compatibility(self, engine_path):
        engine_trt_version = None
        for engine_file in pathlib.Path(engine_path).glob('*.engine'):
            with open(engine_file, "rb") as trt_engine_fhandle:
                engine_trt_version = self._read_trt_engine_version(trt_engine_fhandle)
                break

        if engine_trt_version:
            try:
                installed_trt_libs_version = TrtVersion.from_version_str(metadata.version(TENSORRT_LIBS_PACKAGE_NAME))
            except Exception:
                installed_trt_libs_version = None
                logging.warning(
                    f"Failed to read the currently installed package version for {TENSORRT_LIBS_PACKAGE_NAME},"
                    f"will attempt to continue. If the refit fails, please install the same version of "
                    f"tensorrt and tensorrt_llm as the engine was built with.")

            if installed_trt_libs_version and engine_trt_version != installed_trt_libs_version:
                engine_trt_llm_version = TRT_LLM_VERSION_MAP.get(engine_trt_version, "")
                if engine_trt_llm_version:
                    logging.warning(
                        f"The engine was built with TensorRT {engine_trt_version}, but "
                        f"{TENSORRT_LIBS_PACKAGE_NAME} {installed_trt_libs_version} is installed locally. "
                        f"Will attempt to continue. If the refit fails, please install tensorrt {engine_trt_version}"
                        f" and tensorrt_llm {engine_trt_llm_version} or another compatible version."
                    )
                else:
                    logging.warning(
                        f"The engine was built with TensorRT {engine_trt_version}, but "
                        f"{TENSORRT_LIBS_PACKAGE_NAME} {installed_trt_libs_version} is installed locally. "
                        f"Will attempt to continue. TensorRT {engine_trt_version} is not known to be "
                        f"used by a supported tensorrt_llm release. If the refit fails,"
                        f" please install tensorrt {engine_trt_version} or another compatible version."
                    )

    def _refit_llm(self, checkpoint_path: str, engine_path: str, output_dir: str):
        # Reused the code in main() from tensorrt_llm.commands.refit.
        # If in the future, tensorrt_llm export refit pythong API,
        # need to rewrite this part to use the officially exported API
        try:
            if not os.path.exists(checkpoint_path) or not os.path.exists(engine_path):
                raise ValueError(f"{checkpoint_path} or {engine_path} does not exist.")

            with self._handle_llm_refit_input("checkpoint", checkpoint_path) as checkpoint_dir, \
                    self._handle_llm_refit_input("engine", engine_path) as engine_dir:

                engine_config = EngineConfig.from_json_file(
                    os.path.join(engine_dir, 'config.json')
                )

                with open(os.path.join(checkpoint_dir, 'config.json'), 'r') as f:
                    checkpoint_config = json.load(f)

                if not engine_config.build_config.use_strip_plan:
                    raise ValueError(f"Engine {engine_path} does not appear to have been built with --strip-plan.")

                engine_arch = engine_config.pretrained_config.architecture
                checkpoint_arch = checkpoint_config['architecture']
                if engine_arch != checkpoint_arch:
                    raise RuntimeError(
                        'Engine Architecture and Checkpoint Architecture do not match. ' +
                        f'Engine Architecture: `{engine_arch}`, Checkpoint Architecture: `{checkpoint_arch}`'
                    )

                fixed_wts_in_model = []
                model_cls = MODEL_MAP[engine_arch]
                model = model_cls.from_config(engine_config.pretrained_config)
                for name, param in model.named_parameters():
                    if param.is_inited():
                        fixed_wts_in_model.append(name)

                refit_llm(
                    engine_dir=os.path.normpath(engine_dir),
                    checkpoint_dir=os.path.normpath(checkpoint_dir),
                    engine_config=engine_config,
                    output_dir=os.path.normpath(output_dir),
                    fixed_weights_names=fixed_wts_in_model
                )
        except NameError:
            raise RuntimeError("Failed to import tensorrt_llm, please make sure that TensorRT LLM is installed")
        except Exception:
            raise RuntimeError(f"Failed to refit LLM engine in {engine_path}")

    def refit(self, engine_path: str, model_path: str, model_type: BuildType,
              output_path: str, is_engine_vc: bool = False):
        if platform.system() == "Darwin":
            raise OSError("Darwin based operating system not supported for refit.")

        if model_type is BuildType.ONNX:
            if is_engine_vc:
                logging.info("Engine is VC. Will use lean runtime to refit.")
            logging.info(f"Refitting {engine_path} -> {output_path}")
            self._save_refitted_engine(
                refitted_engine=self._refit_engine(
                    trt_engine=self._load_engine(engine_path, is_engine_vc),
                    onnx_model_path=model_path,
                    is_engine_vc=is_engine_vc
                ),
                output_path=output_path
            )
        elif model_type is BuildType.TRT_LLM:
            if is_engine_vc:
                logging.info("--vc is ignored, only compatible for ONNX models")
            # When we have venv management implemented, the check will happen during venv setup.
            self._check_trtllm_refit_version_compatibility(engine_path)
            self._refit_llm(
                checkpoint_path=model_path,
                engine_path=engine_path,
                output_dir=output_path
            )
