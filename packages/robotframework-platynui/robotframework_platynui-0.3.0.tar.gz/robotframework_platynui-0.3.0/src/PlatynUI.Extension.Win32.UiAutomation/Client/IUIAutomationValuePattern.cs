// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[Guid("A94CD8B1-0844-4CD6-9D2D-640537AB39E9")]
[ComImport]
public interface IUIAutomationValuePattern
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void SetValue([MarshalAs(UnmanagedType.BStr), In] string val);

    [DispId(1610678273)]
    string CurrentValue
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        [return: MarshalAs(UnmanagedType.BStr)]
        get;
    }

    [DispId(1610678274)]
    int CurrentIsReadOnly
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        get;
    }

    [DispId(1610678275)]
    string CachedValue
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        [return: MarshalAs(UnmanagedType.BStr)]
        get;
    }

    [DispId(1610678276)]
    int CachedIsReadOnly
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        get;
    }
}
