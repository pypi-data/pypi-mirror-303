// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[StructLayout(LayoutKind.Sequential, Pack = 8)]
public struct UiaChangeInfo
{
    public int uiaId;

    [MarshalAs(UnmanagedType.Struct)]
    public object payload;

    [MarshalAs(UnmanagedType.Struct)]
    public object extraInfo;
}
