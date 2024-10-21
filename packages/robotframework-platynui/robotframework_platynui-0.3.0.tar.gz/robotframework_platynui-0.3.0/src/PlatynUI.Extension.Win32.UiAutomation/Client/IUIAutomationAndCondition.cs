// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[Guid("A7D0AF36-B912-45FE-9855-091DDC174AEC")]
[ComConversionLoss]
[ComImport]
public interface IUIAutomationAndCondition : IUIAutomationCondition
{
    [DispId(1610743808)]
    int ChildCount
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        get;
    }

    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void GetChildrenAsNativeArray([Out] IntPtr childArray, out int childArrayCount);

    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    [return: MarshalAs(UnmanagedType.SafeArray, SafeArraySubType = VarEnum.VT_UNKNOWN)]
    IUIAutomationCondition[] GetChildren();
}
