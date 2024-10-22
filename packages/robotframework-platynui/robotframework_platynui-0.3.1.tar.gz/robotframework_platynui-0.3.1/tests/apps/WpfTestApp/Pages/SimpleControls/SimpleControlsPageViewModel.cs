// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;
using System.Windows;

namespace WpfTestApp.Pages.SimpleControls;

[Export(typeof(TabPageBase))]
public class SimpleControlsPageViewModel : TabPageBase
{
    private SimpleControlsPageViewModel()
        : base("SimpleControls") { }

    public void DoSomething()
    {
        MessageBox.Show("Done");
    }
}
