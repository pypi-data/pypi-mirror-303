# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

from robotlibcore import keyword

from ..ui import Element


class Mouse:
    @keyword
    def mouse_click(self, locator: Element, text: str) -> None:
        raise NotImplementedError
