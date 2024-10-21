// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client
{
    [Guid("5ED5202E-B2AC-47A6-B638-4B0BF140D78E")]
    [InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
    [ComImport]
    public interface IUIAutomationSelectionPattern
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        [return: MarshalAs(UnmanagedType.Interface)]
        IUIAutomationElementArray GetCurrentSelection();

        [DispId(1610678273)]
        int CurrentCanSelectMultiple
        {
            [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
            get;
        }

        [DispId(1610678274)]
        int CurrentIsSelectionRequired
        {
            [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
            get;
        }

        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        [return: MarshalAs(UnmanagedType.Interface)]
        IUIAutomationElementArray GetCachedSelection();

        [DispId(1610678276)]
        int CachedCanSelectMultiple
        {
            [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
            get;
        }

        [DispId(1610678277)]
        int CachedIsSelectionRequired
        {
            [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
            get;
        }
    }
}
