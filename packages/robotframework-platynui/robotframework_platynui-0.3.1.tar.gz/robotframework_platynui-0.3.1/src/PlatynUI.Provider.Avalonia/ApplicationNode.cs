using System.Diagnostics;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using PlatynUI.Provider.Core;

namespace PlatynUI.Provider.Avalonia;

public class ApplicationNode : Node
{
    public override NodeType NodeType => NodeType.Application;

    public override string LocalName => "Application";

    public override bool IsValid()
    {
        return Application.Current != null;
    }

    private Dictionary<string, Func<object?>>? _attributes = null;

    protected Dictionary<string, Func<object?>> Attributes =>
        _attributes ??= new()
        {
            ["Technology"] = () => "Avalonia",
            ["Role"] = () => new string[] { LocalName },
            ["Name"] = () => Application.Current?.Name,
            ["RuntimeId"] = () => Reference.RuntimeId,
            ["ProcessId"] = () => Environment.ProcessId,
            ["ProcessName"] = () => Process.GetCurrentProcess().ProcessName,
            ["SessionId"] = () => Process.GetCurrentProcess().SessionId,
            ["MainWindowHandle"] = () => Process.GetCurrentProcess().MainWindowHandle,
            ["MainWindowTitle"] = () => Process.GetCurrentProcess().MainWindowTitle,
            ["MainModule.FileName"] = () => Process.GetCurrentProcess().MainModule?.FileName,
            ["MainModule.ModuleName"] = () => Process.GetCurrentProcess().MainModule?.ModuleName,
            ["FileVersionInfo.FileDescription"] = () =>
                Process.GetCurrentProcess().MainModule?.FileVersionInfo.FileDescription,
            ["FileVersionInfo.ProductName"] = () => Process.GetCurrentProcess().MainModule?.FileVersionInfo.ProductName,
            ["FileVersionInfo.InternalName"] = () =>
                Process.GetCurrentProcess().MainModule?.FileVersionInfo.InternalName,
            ["FileVersionInfo.CompanyName"] = () => Process.GetCurrentProcess().MainModule?.FileVersionInfo.CompanyName,
            ["FileVersionInfo.Comments"] = () => Process.GetCurrentProcess().MainModule?.FileVersionInfo.Comments,
            ["FileVersionInfo.FileVersion"] = () => Process.GetCurrentProcess().MainModule?.FileVersionInfo.FileVersion,
            ["FileVersionInfo.ProductVersion"] = () =>
                Process.GetCurrentProcess().MainModule?.FileVersionInfo.ProductVersion,
            ["FileVersionInfo.SpecialBuild"] = () =>
                Process.GetCurrentProcess().MainModule?.FileVersionInfo.SpecialBuild,
            ["FileVersionInfo.IsDebug"] = () => Process.GetCurrentProcess().MainModule?.FileVersionInfo.IsDebug,
            ["RuntimeInformation.FrameworkDescription"] = () =>
                System.Runtime.InteropServices.RuntimeInformation.FrameworkDescription,
        };

    public override string[] GetAttributeNames()
    {
        return [.. Attributes.Keys];
    }

    public override object? GetAttributeValue(string attributeName)
    {
        if (Attributes.TryGetValue(attributeName, out var value))
        {
            try
            {
                return value();
            }
            catch (Exception e)
            {
                Debug.WriteLine(e);
            }
        }
        return null;
    }

    public override string GetAttributeValueType(string attributeName)
    {
        var value = GetAttributeValue(attributeName);
        return value?.GetType().FullName ?? "";
    }

    internal override IEnumerable<Node> GetChildren()
    {
        if (Application.Current?.ApplicationLifetime is IClassicDesktopStyleApplicationLifetime lifetime)
        {
            return lifetime
                .Windows.Select(w => NodeInfo.GetOrCreateNode<ElementNode, Control>(w))
                .Where(n => n != null && n.IsValid());
        }

        return [];
    }
}
