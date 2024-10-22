// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Runtime.InteropServices;

namespace PlatynUI.Extension.Win32.UiAutomation.Client;

[CoClass(typeof(CUIAutomation8Class))]
[Guid("34723AFF-0C9D-49D0-9896-7AB52DF8CD8A")]
[ComImport]
public interface CUIAutomation8 : IUIAutomation2 { }
