// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;

namespace WpfTestApp.Pages.Edits;

[Export(typeof(TabPageBase))]
public class EditsPageViewModel : TabPageBase
{
    private EditsPageViewModel()
        : base("Edits") { }
}
