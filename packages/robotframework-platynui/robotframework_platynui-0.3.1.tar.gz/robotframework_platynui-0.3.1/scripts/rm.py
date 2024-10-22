# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

import os
import shutil
import sys
from typing import Union


def rm(*paths: Union["os.PathLike[str]", str]) -> None:
    for path in paths:
        if not os.path.exists(path):
            continue
        try:
            shutil.rmtree(path)
        except BaseException:
            try:
                os.remove(path)
            except BaseException:
                raise RuntimeError(f"Failed to remove {path!r}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: rm.py <file>")
        sys.exit(1)

    rm(*sys.argv[1:])
