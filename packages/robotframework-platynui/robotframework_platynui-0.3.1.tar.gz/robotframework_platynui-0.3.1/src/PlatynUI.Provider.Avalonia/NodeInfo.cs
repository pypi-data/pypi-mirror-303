using System.Runtime.CompilerServices;

using PlatynUI.Provider.Core;

namespace PlatynUI.Provider.Avalonia;


public class NodeInfo : INodeInfoAsync
{
    protected static readonly ConditionalWeakTable<object, object> _nodes = [];

    public static TNode GetOrCreateNode<TNode>()
        where TNode : Node, new()
    {
        lock (_nodes)
        {
            var t = typeof(TNode);

            if (!_nodes.TryGetValue(t, out var node))
            {
                var reference = new ElementReference([80, 109, typeof(TNode).GetHashCode()]);

                node = new TNode() { Reference = reference };

                _nodes.Add(t, node);
            }

            return (TNode)node;
        }
    }

    public static TNode GetOrCreateNode<TNode, TElement>(TElement element)
        where TNode : Node<TElement>, new()
        where TElement : class
    {
        lock (_nodes)
        {
            if (!_nodes.TryGetValue(element, out var node))
            {
                var reference = new ElementReference([80, 108, element.GetHashCode()]);

                node = new TNode() { Reference = reference, WeakElement = new(element) };

                _nodes.Add(element, node);
            }

            return (TNode)node;
        }
    }

    public static Node? GetNodeFromReference(ElementReference reference)
    {
        return (Node)_nodes.FirstOrDefault(pair => ((Node)pair.Value).Reference == reference).Value;
    }

    public virtual Task<bool> IsValidAsync(ElementReference reference)
    {
        var node = GetNodeFromReference(reference);
        if (node is null)
        {
            return Task.FromResult(false);
        }

        return Task.FromResult(node.IsValid());
    }

    public Task<IList<ElementReference>> GetChildrenAsync(ElementReference parentReference)
    {
        var node = GetNodeFromReference(parentReference);
        if (node is null)
        {
            return Task.FromResult<IList<ElementReference>>([]);
        }

        return Task.FromResult<IList<ElementReference>>(node.GetChildren().Select(v => v.Reference).ToList());
    }

    public Task<string[]> GetAttributeNamesAsync(ElementReference reference)
    {
        var node = GetNodeFromReference(reference);
        if (node == null || !node.IsValid())
        {
            return Task.FromResult<string[]>([]);
        }

        return Task.FromResult(node.GetAttributeNames());
    }

    public Task<object?> GetAttributeValueAsync(ElementReference reference, string attributeName)
    {
        var node = GetNodeFromReference(reference);
        if (node == null || !node.IsValid())
        {
            return Task.FromResult<object?>(null);
        }

        return Task.FromResult(node.GetAttributeValue(attributeName));
    }

    public Task<string> GetAttributeTypeAsync(ElementReference reference, string attributeName)
    {
        var node = GetNodeFromReference(reference);
        if (node == null || !node.IsValid())
        {
            return Task.FromResult("");
        }

        return Task.FromResult(node.GetAttributeValueType(attributeName));
    }

    public virtual Task<string> GetLocalNameAsync(ElementReference reference)
    {
        var node = GetNodeFromReference(reference);
        if (node == null || !node.IsValid())
        {
            return Task.FromResult("Unknown");
        }

        return Task.FromResult(node.LocalName);
    }

    public virtual Task<NodeType> GetNodeTypeAsync(ElementReference reference)
    {
        var node = GetNodeFromReference(reference);
        if (node == null || !node.IsValid())
        {
            return Task.FromResult(NodeType.Unknown);
        }

        return Task.FromResult(node.NodeType);
    }
}
