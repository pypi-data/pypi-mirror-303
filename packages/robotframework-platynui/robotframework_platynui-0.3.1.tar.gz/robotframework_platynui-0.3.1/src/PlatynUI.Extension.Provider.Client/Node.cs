// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Diagnostics;
using Newtonsoft.Json.Linq;
using PlatynUI.Provider.Core;
using PlatynUI.Runtime;
using PlatynUI.Runtime.Core;
using Attribute = PlatynUI.Runtime.Core.Attribute;

namespace PlatynUI.Extension.Provider.Client;

public class Node(INode? parent, ElementReference reference, ProcessProvider provider) : INode
{
    public ElementReference Reference { get; } = reference;
    public ProcessProvider Provider { get; } = provider;

    public INode? Parent { get; } = parent;

    private List<INode>? _children = null;
    public IList<INode> Children => _children ??= GetChildren();

    protected virtual List<INode> GetChildren()
    {
        return Provider
            .NodeInfo.GetChildren(Reference)
            .Select(childReference => (INode)new Node(this, childReference, Provider))
            .ToList();
    }

    public string? _localName = null;
    public string LocalName => _localName ??= Provider.NodeInfo.GetLocalName(Reference);

    private string? _namespaceURI = null;
    public string NamespaceURI
    {
        get
        {
            if (_namespaceURI is null)
            {
                var nodeType = Provider.NodeInfo.GetNodeType(Reference);

                _namespaceURI = nodeType switch
                {
                    NodeType.Application => Namespaces.App,
                    NodeType.Item => Namespaces.Item,
                    _ => Namespaces.Raw,
                };
            }
            return _namespaceURI;
        }
    }

    public Dictionary<string, IAttribute>? _attributes = null;
    public IDictionary<string, IAttribute> Attributes => _attributes ??= GetAttributes();

    protected virtual Dictionary<string, IAttribute> GetAttributes()
    {
        var attributeNames = Provider.NodeInfo.GetAttributeNames(Reference);
        var result = attributeNames
            .Select(attributeName =>
                (IAttribute)
                    new Attribute(
                        attributeName,
                        () =>
                        {
                            var value = Provider.NodeInfo.GetAttributeValue(Reference, attributeName);
                            if (value is JToken jToken)
                            {
                                try
                                {
                                    var typeName = Provider.NodeInfo.GetAttributeType(Reference, attributeName);
                                    var type = Type.GetType(typeName);
                                    if (type is not null)
                                    {
                                        return jToken.ToObject(type);
                                    }
                                }
                                catch (Exception e)
                                {
                                    Debug.WriteLine(e);
                                }
                            }
                            return value;
                        }
                    )
            )
            .OrderBy(attribute => attribute.Name)
            .ToDictionary(attribute => attribute.Name);

        return result;
    }

    public INode Clone()
    {
        return new Node(Parent, Reference, Provider);
    }

    public bool IsSamePosition(INode other)
    {
        return other switch
        {
            Node node => Reference == node.Reference,
            _ => false
        };
    }

    public void Invalidate()
    {
        _localName = null;
        _namespaceURI = null;
        _attributes = null;
        _children = null;
    }
}

class ApplicationNode(INode? parent, ElementReference reference, ProcessProvider provider)
    : Node(parent, reference, provider)
{
    protected override List<INode> GetChildren()
    {
        return Provider
            .NodeInfo.GetChildren(Reference)
            .Select(childReference => (INode)new ElementNode(this, childReference, Provider))
            .ToList();
    }
}

class ElementNode(INode? parent, ElementReference reference, ProcessProvider provider)
    : Node(parent, reference, provider),
        IElement
{
    protected override List<INode> GetChildren()
    {
        return Provider
            .NodeInfo.GetChildren(Reference)
            .Select(childReference => (INode)new ElementNode(this, childReference, Provider))
            .ToList();
    }

    protected T? GetAttribute<T>(string name)
    {
        if (Attributes.TryGetValue(name, out var attribute))
        {
            return (T?)attribute.Value;
        }
        return default;
    }

    public bool TryEnsureVisible()
    {
        throw new NotImplementedException();
    }

    public bool TryEnsureApplicationIsReady()
    {
        throw new NotImplementedException();
    }

    public bool TryEnsureToplevelParentIsActive()
    {
        throw new NotImplementedException();
    }

    public bool TryBringIntoView()
    {
        throw new NotImplementedException();
    }

    public bool IsEnabled => GetAttribute<bool?>("IsEnabled") ?? false;

    public bool IsVisible => GetAttribute<bool?>("IsVisible") ?? false;
    public bool IsInView => GetAttribute<bool?>("IsInView") ?? false;

    public bool TopLevelParentIsActive => GetAttribute<bool?>("TopLevelParentIsActive") ?? false;

    public Rect BoundingRectangle
    {
        get
        {
            var data = GetAttribute<double[]?>("BoundingRectangle");
            if (data is not null && data.Length == 4)
            {
                return new Rect(data[0], data[1], data[2], data[3]);
            }
            return Rect.Empty;
        }
    }

    public Rect VisibleRectangle => GetAttribute<Rect?>("VisibleRectangle") ?? Rect.Empty;

    public Point? DefaultClickPosition => GetAttribute<Point?>("DefaultClickPosition") ?? Point.Empty;
}
