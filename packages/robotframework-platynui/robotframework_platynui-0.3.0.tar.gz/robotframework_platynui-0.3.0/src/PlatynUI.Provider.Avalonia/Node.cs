using PlatynUI.Provider.Core;

namespace PlatynUI.Provider.Avalonia;

public abstract class Node
{
    private ElementReference? _nodeReference = null;
    public ElementReference Reference
    {
        get => _nodeReference ?? throw new InvalidOperationException($"{nameof(Reference)} not set.");
        set => _nodeReference = value;
    }

    public abstract NodeType NodeType { get; }

    public abstract bool IsValid();
    public abstract string[] GetAttributeNames();
    public abstract object? GetAttributeValue(string attributeName);
    public abstract string GetAttributeValueType(string attributeName);
    public abstract string LocalName { get; }

    internal abstract IEnumerable<Node> GetChildren();
}

public abstract class Node<TElement> : Node
    where TElement : class
{
    public Node() { }

    public Node(ElementReference reference, TElement element)
    {
        Reference = reference;
        WeakElement = new(element);
    }

    private WeakReference<TElement>? _weakElement = null;
    public WeakReference<TElement> WeakElement
    {
        get => _weakElement ?? throw new InvalidOperationException($"{nameof(WeakElement)} not set.");
        set => _weakElement = value;
    }

    public TElement? Element => WeakElement.TryGetTarget(out var element) ? element : null;
}
