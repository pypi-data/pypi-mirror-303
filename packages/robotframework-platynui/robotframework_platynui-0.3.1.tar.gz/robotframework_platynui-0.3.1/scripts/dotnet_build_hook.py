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

    def _run_shell(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=None if self.app.verbosity else subprocess.DEVNULL,
            # stderr=None if self.app.verbosity else subprocess.DEVNULL,
        )

    def initialize(self, version: str, build_data: Dict[str, Any]) -> None:
        self._run_shell("dotnet restore")
        self._run_shell(
            "dotnet publish -c release -f net8.0 -p:DebugSymbols=false -P:DebugType=None "
            f"-o {self.BASE_OUTPUT_DIR / 'coreclr'} ./src/PlatynUI.Spy"
        )
        self._run_shell(
            "dotnet publish -c release -f net8.0 -p:DebugSymbols=false -P:DebugType=None "
            f"-o {self.BASE_PROVIDERS_DIR / 'avalonia'} ./src/PlatynUI.Provider.Avalonia",
        )

    def clean(self, versions: List[str]) -> None:
        self._run_shell("dotnet clean -c release")
        rm(self.BASE_OUTPUT_DIR / "coreclr")
