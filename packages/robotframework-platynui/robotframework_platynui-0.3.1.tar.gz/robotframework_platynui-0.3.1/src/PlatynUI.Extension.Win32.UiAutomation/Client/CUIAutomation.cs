// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.InteropServices;

namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[CoClass(typeof(CUIAutomationClass))]
[Guid("30CBE57D-D9D0-452A-AB13-7AC5AC4825EE")]
[ComImport]
#pragma warning disable IDE1006 // Naming Styles
public interface CUIAutomation : IUIAutomation { }
#pragma warning restore IDE1006 // Naming Styles
