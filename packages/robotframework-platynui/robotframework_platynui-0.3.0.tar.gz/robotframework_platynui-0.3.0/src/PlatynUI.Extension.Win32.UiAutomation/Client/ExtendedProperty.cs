// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[StructLayout(LayoutKind.Sequential, Pack = 8)]
public struct ExtendedProperty
{
    [MarshalAs(UnmanagedType.BStr)]
    public string PropertyName;

    [MarshalAs(UnmanagedType.BStr)]
    public string PropertyValue;
}
