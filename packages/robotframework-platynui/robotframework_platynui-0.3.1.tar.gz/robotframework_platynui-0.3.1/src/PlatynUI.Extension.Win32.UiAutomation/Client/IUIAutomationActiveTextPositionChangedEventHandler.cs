// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[Guid("F97933B0-8DAE-4496-8997-5BA015FE0D82")]
[TypeLibType(TypeLibTypeFlags.FOleAutomation)]
[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[ComImport]
public interface IUIAutomationActiveTextPositionChangedEventHandler
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void HandleActiveTextPositionChangedEvent(
        [MarshalAs(UnmanagedType.Interface), In] IUIAutomationElement sender,
        [MarshalAs(UnmanagedType.Interface), In] IUIAutomationTextRange range
    );
}
