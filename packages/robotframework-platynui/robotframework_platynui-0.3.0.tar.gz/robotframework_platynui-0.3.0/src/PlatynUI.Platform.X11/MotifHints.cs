// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Platform.X11;

public struct MotifHints
{
    public uint Flags;
    public uint Functions;
    public uint Decorations;
    public uint inputMode;
    public uint status;

    public static uint MWM_HINTS_FUNCTIONS = 1 << 0;

    public static uint MWM_FUNC_ALL = 1 << 0;
    public static uint MWM_FUNC_RESIZE = 1 << 1;
    public static uint MWM_FUNC_MOVE = 1 << 2;
    public static uint MWM_FUNC_MINIMIZE = 1 << 3;
    public static uint MWM_FUNC_MAXIMIZE = 1 << 4;
    public static uint MWM_FUNC_CLOSE = 1 << 5;

    public static uint MWM_HINTS_DECORATIONS = 1 << 1;

    public static uint MWM_DECOR_ALL = 1 << 0;
    public static uint MWM_DECOR_BORDER = 1 << 1;
    public static uint MWM_DECOR_RESIZEH = 1 << 2;
    public static uint MWM_DECOR_TITLE = 1 << 3;
    public static uint MWM_DECOR_MENU = 1 << 4;
    public static uint MWM_DECOR_MINIMIZE = 1 << 5;
    public static uint MWM_DECOR_MAXIMIZE = 1 << 6;
};
