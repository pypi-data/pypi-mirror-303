// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using Avalonia.Controls;
using Avalonia.Interactivity;
using FluentAvalonia.UI.Windowing;

namespace PlatynUI.Spy.Views;

public partial class MainWindow : AppWindow
{
    public MainWindow()
    {
        TitleBar.ExtendsContentIntoTitleBar = true;
        TitleBar.TitleBarHitTestType = TitleBarHitTestType.Complex;

        InitializeComponent();
    }

    protected override void OnLoaded(RoutedEventArgs e)
    {
        base.OnLoaded(e);

        if (VisualRoot is AppWindow aw)
        {
            TitleBarHost.ColumnDefinitions[4].Width = new GridLength(aw.TitleBar.RightInset, GridUnitType.Pixel);
        }
    }
}
