// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Extension.Win32.UiAutomation.Client;

public enum NotificationKind
{
    NotificationKind_ItemAdded,
    NotificationKind_ItemRemoved,
    NotificationKind_ActionCompleted,
    NotificationKind_ActionAborted,
    NotificationKind_Other,
}
