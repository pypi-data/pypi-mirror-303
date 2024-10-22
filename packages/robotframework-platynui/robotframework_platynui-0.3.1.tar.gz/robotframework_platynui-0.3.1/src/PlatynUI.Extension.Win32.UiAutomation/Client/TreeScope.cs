// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Extension.Win32.UiAutomation.Client;

public enum TreeScope
{
    TreeScope_None = 0,
    TreeScope_Element = 1,
    TreeScope_Children = 2,
    TreeScope_Descendants = 4,
    TreeScope_Subtree = 7,
    TreeScope_Parent = 8,
    TreeScope_Ancestors = 16, // 0x00000010
}
