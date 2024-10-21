using System.Diagnostics;
using Avalonia;
using Avalonia.Automation.Peers;
using Avalonia.Controls;
using Avalonia.Threading;
using Avalonia.VisualTree;
using PlatynUI.Provider.Core;

namespace PlatynUI.Provider.Avalonia;

internal class ElementNode : Node<Control>
{
    public override NodeType NodeType => NodeType.Element;

    public override string LocalName => Element?.GetType().Name ?? "Unknown";

    private Dictionary<string, Func<object?>>? _attributes = null;

    protected Dictionary<string, Func<object?>> Attributes => _attributes ??= GetAttributes();

    private static Rect GetBounds(Control control)
    {
        var root = control.GetVisualRoot();

        if (root is not Visual rootVisual)
            return default;

        var transform = control.TransformToVisual(rootVisual);

        if (!transform.HasValue)
            return default;

        return new Rect(control.Bounds.Size).TransformToAABB(transform.Value);
    }

    private static IEnumerable<string> YieldSupportedRoles(object? control)
    {
        var type = control?.GetType();
        while (type != null)
        {
            yield return type.Name;
            type = type.BaseType;
        }
    }

    private Dictionary<string, Func<object?>> GetAttributes()
    {
        var result = new Dictionary<string, Func<object?>>
        {
            ["Name"] = () => Element?.Name,
            ["Role"] = () => new string[] { LocalName },
            ["SupportedRoles"] = () => YieldSupportedRoles(Element).ToArray(),
            ["AutomationId"] = () => Dispatcher.UIThread.Invoke(() => AutomationPeer?.GetAutomationId()),
            ["ClassName"] = () => Element?.GetType().ToString() ?? "",
            ["BoundingRectangle"] = () =>
            {
                var pr = Dispatcher.UIThread.Invoke<Rect?>(() =>
                {
                    if (Element == null || AutomationPeer == null)
                    {
                        return null;
                    }

                    var r = GetBounds(Element);

                    var root = Element.GetVisualRoot();

                    if (root == null)
                    {
                        return null;
                    }

                    return new PixelRect(root.PointToScreen(r.TopLeft), root.PointToScreen(r.BottomRight)).ToRect(1);
                });

                if (!pr.HasValue)
                    return null;

                return new double[] { pr.Value.X, pr.Value.Y, pr.Value.Width, pr.Value.Height };
            },
            ["IsEnabled"] = () => Dispatcher.UIThread.Invoke(() => Element?.IsEnabled) ?? false,
            ["IsVisible"] = () => Dispatcher.UIThread.Invoke(() => Element?.IsVisible) ?? false,
            ["IsFocused"] = () => Dispatcher.UIThread.Invoke(() => Element?.IsFocused) ?? false,

            ["IsHitTestVisible"] = () => Dispatcher.UIThread.Invoke(() => Element?.IsHitTestVisible) ?? false,
        };

        if (Element != null)
        {
            foreach (
                var prop in AvaloniaPropertyRegistry
                    .Instance.GetRegistered(Element)
                    .Union(AvaloniaPropertyRegistry.Instance.GetRegisteredAttached(Element.GetType()))
            )
            {
                if (result.ContainsKey("Native.Registered." + prop.Name))
                {
                    continue;
                }
                result.Add(
                    "Native.Registered." + prop.Name,
                    () => Dispatcher.UIThread.Invoke(() => Element.GetValue(prop))
                );
            }

            foreach (var prop in Element.GetType().GetProperties().Where(x => x.GetIndexParameters().Length == 0))
            {
                if (result.ContainsKey("Native.Clr." + prop.Name))
                {
                    continue;
                }

                result.Add("Native.Clr." + prop.Name, () => Dispatcher.UIThread.Invoke(() => prop.GetValue(Element)));
            }
        }

        return result;
    }

    public AutomationPeer? _automationPeer = null;
    public AutomationPeer? AutomationPeer =>
        _automationPeer ??=
            Element != null
                ? Dispatcher.UIThread.Invoke(() => ControlAutomationPeer.CreatePeerForElement(Element))
                : null;

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
                Debug.WriteLine($"Error getting value for `{attributeName}`: {e}");
            }
        }
        return null;
    }

    public override string GetAttributeValueType(string attributeName)
    {
        var value = GetAttributeValue(attributeName);
        return value?.GetType().FullName ?? "";
    }

    public override bool IsValid()
    {
        return Element != null;
    }

    internal override IEnumerable<Node> GetChildren()
    {
        if (Element == null)
        {
            return [];
        }

        return Element
            .GetVisualChildren()
            .Cast<Control>()
            .Select(e => NodeInfo.GetOrCreateNode<ElementNode, Control>(e))
            .Where(n => n != null && n.IsValid());
    }
}
