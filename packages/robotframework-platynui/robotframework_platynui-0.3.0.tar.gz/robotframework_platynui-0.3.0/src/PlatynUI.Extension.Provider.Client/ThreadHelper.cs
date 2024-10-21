// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using Microsoft.VisualStudio.Threading;

namespace PlatynUI.Extension.Provider.Client;

class ThreadHelper
{
    public static readonly JoinableTaskContext JoinableTaskContext = new();
    public static readonly JoinableTaskFactory JoinableTaskFactory = new(JoinableTaskContext);
}
