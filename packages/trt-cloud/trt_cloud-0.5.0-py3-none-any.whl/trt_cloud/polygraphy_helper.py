# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import io
import traceback
from contextlib import redirect_stderr, redirect_stdout
from enum import Enum
from typing import List, Tuple

import polygraphy.tools


class PolygraphyTool(Enum):
    SURGEON = "surgeon"


class PolyGraphyCallResult(Enum):
    OKAY = 0
    ERROR = 1


class PolygraphyToolHelper:
    def __init__(self, polygraphy_tool: PolygraphyTool):
        self.polygraphy_tool = polygraphy_tool

    def run(self, args: List[str]) -> Tuple[PolyGraphyCallResult, str]:
        polygraphy_output = io.StringIO()
        with redirect_stdout(polygraphy_output), redirect_stderr(polygraphy_output):
            try:
                polygraphy.tools.main(run_opts=[self.polygraphy_tool.value, *args])
            except Exception:
                polygraphy_output.write(traceback.format_exc())
                return PolyGraphyCallResult.ERROR, polygraphy_output.getvalue()

            return PolyGraphyCallResult.OKAY, polygraphy_output.getvalue()
