// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client
{
    [Guid("40CD37D4-C756-4B0C-8C6F-BDDFEEB13B50")]
    [InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
    [TypeLibType(TypeLibTypeFlags.FOleAutomation)]
    [ComImport]
    public interface IUIAutomationPropertyChangedEventHandler
    {
        [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
        void HandlePropertyChangedEvent(
            [MarshalAs(UnmanagedType.Interface), In] IUIAutomationElement sender,
            [In] int propertyId,
            [MarshalAs(UnmanagedType.Struct), In] object newValue
        );
    }
}
