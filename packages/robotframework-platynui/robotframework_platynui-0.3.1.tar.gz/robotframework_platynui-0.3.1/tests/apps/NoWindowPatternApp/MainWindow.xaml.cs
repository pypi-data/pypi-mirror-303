// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Text;
using System.Windows;
using System.Windows.Automation.Peers;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace NoWindowPatternApp;

public class CustomWindowAutomationPeer : AutomationPeer
{
    public CustomWindowAutomationPeer(MainWindow mainWindow)
    {
        MainWindow = mainWindow;
    }

    public MainWindow MainWindow { get; }

    public override object GetPattern(PatternInterface patternInterface)
    {
        throw new NotImplementedException();
    }

    protected override string GetAcceleratorKeyCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetAccessKeyCore()
    {
        throw new NotImplementedException();
    }

    protected override AutomationControlType GetAutomationControlTypeCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetAutomationIdCore()
    {
        throw new NotImplementedException();
    }

    protected override Rect GetBoundingRectangleCore()
    {
        throw new NotImplementedException();
    }

    protected override List<AutomationPeer> GetChildrenCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetClassNameCore()
    {
        throw new NotImplementedException();
    }

    protected override Point GetClickablePointCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetHelpTextCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetItemStatusCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetItemTypeCore()
    {
        throw new NotImplementedException();
    }

    protected override AutomationPeer GetLabeledByCore()
    {
        throw new NotImplementedException();
    }

    protected override string GetNameCore()
    {
        throw new NotImplementedException();
    }

    protected override AutomationOrientation GetOrientationCore()
    {
        throw new NotImplementedException();
    }

    protected override bool HasKeyboardFocusCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsContentElementCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsControlElementCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsEnabledCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsKeyboardFocusableCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsOffscreenCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsPasswordCore()
    {
        throw new NotImplementedException();
    }

    protected override bool IsRequiredForFormCore()
    {
        throw new NotImplementedException();
    }

    protected override void SetFocusCore()
    {
        throw new NotImplementedException();
    }
}

/// <summary>
/// Interaction logic for MainWindow.xaml
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    private void Button_Click(object sender, RoutedEventArgs e)
    {
        Close();
    }

    protected override AutomationPeer OnCreateAutomationPeer()
    {
        return new CustomWindowAutomationPeer(this);
    }
}
