# SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
#
# SPDX-License-Identifier: Apache-2.0

from robot.utils import secs_to_timestr


class TimeSpan:
    def __init__(self, seconds: float) -> None:
        self.seconds = seconds

    def __str__(self) -> str:
        return str(secs_to_timestr(self.seconds))
