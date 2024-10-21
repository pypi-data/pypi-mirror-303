// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[Guid("619BE086-1F4E-4EE4-BAFA-210128738730")]
[ComImport]
public interface IUIAutomationExpandCollapsePattern
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void Expand();

    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void Collapse();

    [DispId(1610678274)]
    ExpandCollapseState CurrentExpandCollapseState
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        get;
    }

    [DispId(1610678275)]
    ExpandCollapseState CachedExpandCollapseState
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        get;
    }
}
