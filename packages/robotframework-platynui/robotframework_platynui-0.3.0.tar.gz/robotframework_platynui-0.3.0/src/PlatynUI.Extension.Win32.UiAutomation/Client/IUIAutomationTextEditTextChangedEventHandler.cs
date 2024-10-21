// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

#nullable disable
namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[TypeLibType(TypeLibTypeFlags.FOleAutomation)]
[InterfaceType(ComInterfaceType.InterfaceIsIUnknown)]
[Guid("92FAA680-E704-4156-931A-E32D5BB38F3F")]
[ComImport]
public interface IUIAutomationTextEditTextChangedEventHandler
{
    [MethodImpl(MethodImplOptions.InternalCall, MethodCodeType = MethodCodeType.Runtime)]
    void HandleTextEditTextChangedEvent(
        [MarshalAs(UnmanagedType.Interface), In] IUIAutomationElement sender,
        [In] TextEditChangeType TextEditChangeType,
        [MarshalAs(UnmanagedType.SafeArray, SafeArraySubType = VarEnum.VT_BSTR), In] string[] eventStrings
    );
}
