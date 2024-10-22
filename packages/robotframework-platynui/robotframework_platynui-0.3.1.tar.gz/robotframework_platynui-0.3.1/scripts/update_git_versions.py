# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

import contextlib
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, List

if __name__ == "__main__" and not __package__:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[1]

    if str(top) not in sys.path:
        sys.path.append(str(top))

    with contextlib.suppress(ValueError):
        sys.path.remove(str(parent))

    __package__ = "scripts"


from scripts.tools import get_version


def replace_in_file(filename: Path, pattern: "re.Pattern[str]", to: str) -> None:
    text = filename.read_text()
    new = pattern.sub(to, text)
    filename.write_text(new)


def run(title: str, *args: Any, **kwargs: Any) -> None:
    try:
        print(f"running {title}")
        subprocess.run(*args, **kwargs)
    except (SystemExit, KeyboardInterrupt):
        raise
    except BaseException as e:
        print(f"{title} failed: {e}", file=sys.stderr)


def main() -> None:
    version = get_version()
    python_version_files: List[Path] = list(Path().rglob("__about__.py"))

    for f in python_version_files:
        replace_in_file(
            f,
            re.compile(r"""(^_*version_*\s*=\s*['"])([^'"]*)(['"])""", re.MULTILINE),
            rf"\g<1>{version or ''}\g<3>",
        )

    csproj_version_files: List[Path] = [*list(Path().rglob("*.csproj")), *list(Path().rglob("Directory.Build.props"))]

    for f in csproj_version_files:
        replace_in_file(
            f,
            re.compile(r"""(^\s*<Version>)([^<]*)(</Version>)""", re.MULTILINE),
            rf"\g<1>{version or ''}\g<3>",
        )


if __name__ == "__main__":
    main()
