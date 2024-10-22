# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

from robotlibcore import keyword


class Text:
    @keyword
    def set_text(self, locator: str, text: str) -> None:
        locator.set_text(text)
