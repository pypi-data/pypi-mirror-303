// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[Guid("FB377FBE-8EA6-46D5-9C73-6499642D3059")]
[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[ComImport]
public interface IUIAutomationInvokePattern
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void Invoke();
}
