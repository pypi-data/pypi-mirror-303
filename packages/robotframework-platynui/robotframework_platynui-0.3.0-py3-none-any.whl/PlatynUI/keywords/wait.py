# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

from typing import Union

from robotlibcore import keyword

from ..ui import Element
from .types import TimeSpan

__all__ = ["Wait"]


class Wait:
    @keyword
    def ensure_exists(
        self, element: Element, timeout: Union[TimeSpan, float, None] = None, raise_exception: bool = True
    ) -> bool:

        return element.exists(
            timeout=timeout.seconds if isinstance(timeout, TimeSpan) else timeout, raise_exception=raise_exception
        )
