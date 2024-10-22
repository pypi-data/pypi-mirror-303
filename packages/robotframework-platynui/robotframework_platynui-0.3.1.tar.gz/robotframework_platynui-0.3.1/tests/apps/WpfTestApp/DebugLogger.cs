// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System;
using System.Diagnostics;
using Caliburn.Micro;

namespace WpfTestApp;

public class DebugLogger : ILog
{
    private readonly Type _type;

    public DebugLogger(Type type)
    {
        _type = type;
    }

    public void Info(string format, params object[] args)
    {
        Debug.WriteLine($"INFO [{_type}]: {string.Format(format, args)}");
    }

    public void Warn(string format, params object[] args)
    {
        Debug.WriteLine($"WARN [{_type}]: {string.Format(format, args)}");
    }

    public void Error(Exception exception)
    {
        Debug.WriteLine($"ERROR [{_type}]: {exception}");
    }
}
