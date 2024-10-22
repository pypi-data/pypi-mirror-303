// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Extension.Win32.UiAutomation.Client;

public enum SynchronizedInputType
{
    SynchronizedInputType_KeyUp = 1,
    SynchronizedInputType_KeyDown = 2,
    SynchronizedInputType_LeftMouseUp = 4,
    SynchronizedInputType_LeftMouseDown = 8,
    SynchronizedInputType_RightMouseUp = 16, // 0x00000010
    SynchronizedInputType_RightMouseDown = 32, // 0x00000020
}
