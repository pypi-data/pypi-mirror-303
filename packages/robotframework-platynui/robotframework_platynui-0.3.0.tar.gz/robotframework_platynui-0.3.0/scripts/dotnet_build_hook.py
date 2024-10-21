# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

import contextlib
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List

from hatchling.builders.config import BuilderConfig
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]

if str(top) not in sys.path:
    sys.path.append(str(top))

with contextlib.suppress(ValueError):
    sys.path.remove(str(parent))

__package__ = "scripts"

from scripts.rm import rm  # noqa: E402


class DotNetBuildHook(BuildHookInterface[BuilderConfig]):
    BASE_OUTPUT_DIR = Path("src/PlatynUI/ui/runtime")
    BASE_PROVIDERS_DIR = Path("src/PlatynUI/ui/runtime/providers")

    def initialize(self, version: str, build_data: Dict[str, Any]) -> None:
        print("Build Dotnet Runtime")
        subprocess.run("dotnet restore", shell=True, check=True)
        subprocess.run(
            "dotnet publish -c release -f net8.0 -p:DebugSymbols=false -P:DebugType=None "
            f"-o {self.BASE_OUTPUT_DIR / 'coreclr'} ./src/PlatynUI.Spy",
            shell=True,
            check=True,
        )
        subprocess.run(
            "dotnet publish -c release -f net8.0 -p:DebugSymbols=false -P:DebugType=None "
            f"-o {self.BASE_PROVIDERS_DIR / 'avalonia'} ./src/PlatynUI.Provider.Avalonia",
            shell=True,
            check=True,
        )

    def clean(self, versions: List[str]) -> None:
        print("Clean Dotnet Runtime")
        subprocess.check_output("dotnet clean -c release", shell=True)
        rm(self.BASE_OUTPUT_DIR / "coreclr")
