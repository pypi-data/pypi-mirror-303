// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[StructLayout(LayoutKind.Sequential, Pack = 4)]
#pragma warning disable IDE1006 // Naming Styles
public struct tagPOINT
#pragma warning restore IDE1006 // Naming Styles
{
    public int x;
    public int y;
}
