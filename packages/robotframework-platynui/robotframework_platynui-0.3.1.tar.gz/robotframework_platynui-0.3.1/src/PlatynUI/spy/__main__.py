# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

import logging
import os
import subprocess
import warnings
from pathlib import Path

logger = logging.getLogger(__name__)
LOGLEVEL = os.environ.get("LOGLEVEL", None)
if LOGLEVEL:
    logging.basicConfig(level=LOGLEVEL.upper())


def main() -> None:
    from pythonnet import load

    load("coreclr")
    import clr  # noqa: F401
    from pythonnet import get_runtime_info

    rt_kind = get_runtime_info().kind
    logger.debug(f"Runtime kind: {rt_kind}")  # noqa: G004

    if rt_kind == "CoreCLR":
        kind = "coreclr"
    elif rt_kind == ".NET Framework":
        kind = "netfx"
    else:
        warnings.warn(f"Unsupported runtime: {get_runtime_info().kind}")
        raise RuntimeError(f"Unsupported runtime: {get_runtime_info().kind}")

    if os.name == "nt":
        exe_name = "PlatynUI.Spy.exe"
    else:
        exe_name = "PlatynUI.Spy"

    debug_path = Path(__file__).parent / f"../../PlatynUI.Spy/bin/Debug/net8.0/{exe_name}"
    runtime_path = Path(__file__).parent.parent / f"ui/runtime/{kind}/{exe_name}"

    if debug_path.exists():
        logger.debug(f"Starting {exe_name} from {debug_path}")  # noqa: G004
        subprocess.run([debug_path])
    elif runtime_path.exists():
        logger.debug(f"Starting {exe_name} from {runtime_path}")  # noqa: G004
        subprocess.run([runtime_path])
    else:
        print(f"Can't find the executable {exe_name} in the debug or runtime folder.")


if __name__ == "__main__":
    main()
