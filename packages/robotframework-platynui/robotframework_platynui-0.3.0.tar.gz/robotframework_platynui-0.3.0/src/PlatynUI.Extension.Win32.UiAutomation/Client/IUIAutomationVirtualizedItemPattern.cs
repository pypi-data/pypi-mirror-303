// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[Guid("6BA3D7A6-04CF-4F11-8793-A8D1CDE9969F")]
[ComImport]
public interface IUIAutomationVirtualizedItemPattern
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void Realize();
}
