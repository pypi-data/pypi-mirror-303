// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Runtime.Core;

public interface IAdapter
{
    string Id { get; }
    string Name { get; }
    string Role { get; }

    string ClassName { get; }

    string[] SupportedRoles { get; }

    string Type { get; }
    string[] SupportedTypes { get; }

    string FrameworkId { get; }
    string RuntimeId { get; }

    bool IsValid();
    void Invalidate();
}
