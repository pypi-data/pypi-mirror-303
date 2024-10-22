// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Diagnostics;

namespace PlatynUI.Platform.X11.Interop;

[AttributeUsage(
    AttributeTargets.Struct
        | AttributeTargets.Enum
        | AttributeTargets.Property
        | AttributeTargets.Field
        | AttributeTargets.Parameter
        | AttributeTargets.ReturnValue,
    AllowMultiple = false,
    Inherited = true
)]
[Conditional("DEBUG")]
internal sealed partial class NativeTypeNameAttribute(string name) : Attribute
{
    public string Name { get; } = name;
}
