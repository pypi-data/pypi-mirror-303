// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Collections;

namespace PlatynUI.Runtime.Core;

public interface IAttribute
{
    string Name { get; }
    object? Value { get; }
    string NamespaceURI { get; }
}

public class Attribute : IAttribute
{
    public Attribute(string name, Func<object?> valueGetter, string namespaceURI = Namespaces.Raw)
    {
        Name = name;
        _value = null;
        _valueGetter = valueGetter;
        NamespaceURI = namespaceURI;
    }

    public Attribute(string name, object? value, string namespaceURI = Namespaces.Raw)
    {
        Name = name;
        _value = value;
        NamespaceURI = namespaceURI;
    }

    private readonly Func<object?>? _valueGetter;
    private readonly object? _value;

    public string Name { get; }

    private object? GetValue()
    {
        try
        {
            return _valueGetter != null ? _valueGetter() : _value;
        }
        catch
        {
            return null;
        }
    }

    public object? Value => _valueGetter != null ? GetValue() : _value;

    public string NamespaceURI { get; }
}

public interface IAttributesEnumerator : IEnumerator<IAttribute> { }

public class AttributesEnumerator<T>(IEnumerable<T> attributes) : IAttributesEnumerator
    where T : IAttribute
{
    private readonly IEnumerator<T> _enumerator = attributes.GetEnumerator();

    public IAttribute Current => _enumerator.Current;

    object IEnumerator.Current => _enumerator.Current;

    public virtual void Dispose()
    {
        GC.SuppressFinalize(this);
        _enumerator.Dispose();
    }

    public bool MoveNext() => _enumerator.MoveNext();

    public void Reset() => _enumerator.MoveNext();
}

public interface INode
{
    object? UnderlyingObject => this;

    INode? Parent { get; }

    IList<INode> Children { get; }

    void Invalidate();

    virtual IList<INode> GetAncestors()
    {
        var result = new List<INode>();
        INode? current = Parent;
        while (current != null)
        {
            result.Insert(0, current);
            current = current.Parent;
        }
        return result;
    }

    virtual INode? GetFirstChild()
    {
        return Children.FirstOrDefault();
    }

    virtual INode? GetLastChild()
    {
        return Children.LastOrDefault();
    }

    virtual INode? GetNextSibling()
    {
        if (Parent == null)
            return default;

        var siblings = Parent.Children;
        int index = siblings.IndexOf(this);
        return (index >= 0 && index < siblings.Count - 1) ? siblings[index + 1] : null;
    }

    virtual INode? GetPreviousSibling()
    {
        if (Parent == null)
            return null;

        var siblings = Parent.Children;
        int index = siblings.IndexOf(this);
        return (index > 0) ? siblings[index - 1] : null;
    }
    string LocalName { get; }
    string NamespaceURI { get; }

    INode Clone();
    bool IsSamePosition(INode other);

    IDictionary<string, IAttribute> Attributes { get; }

    IAttributesEnumerator GetAttributesEnumerator()
    {
        return new AttributesEnumerator<IAttribute>(Attributes.Values);
    }
}

public interface INodeProvider
{
    IEnumerable<INode> GetNodes(INode parent);
}
