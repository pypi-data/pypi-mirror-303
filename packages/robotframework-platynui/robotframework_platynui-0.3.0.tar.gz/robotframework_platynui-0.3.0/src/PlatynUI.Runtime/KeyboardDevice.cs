// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;
using PlatynUI.Runtime.Core;

namespace PlatynUI.Runtime;

public class KeyboardDevice
{
    [Import]
    protected IKeyboardDevice? keyboardDevice;

    private KeyboardDevice()
    {
        PlatynUiExtensions.ComposeParts(this);
    }

    private static KeyboardDevice? _instance;
    private static KeyboardDevice Instance => _instance ??= new KeyboardDevice();

    public static Keycode KeyToKeyCode(object? key)
    {
        return Instance.keyboardDevice?.KeyToKeyCode(key) ?? new Keycode(null, null, false, "No keyboard device found");
    }

    public static bool SendKeyCode(object keyCode, bool pressed)
    {
        return Instance.keyboardDevice?.SendKeyCode(keyCode, pressed) ?? false;
    }


}
