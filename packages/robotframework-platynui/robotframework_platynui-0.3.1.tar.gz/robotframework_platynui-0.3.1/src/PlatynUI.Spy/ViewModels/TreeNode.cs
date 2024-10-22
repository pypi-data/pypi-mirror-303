// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using PlatynUI.Runtime.Core;
using ReactiveUI;

namespace PlatynUI.Spy.ViewModels;

public class TreeNodeAttribute(string name, object? value) : ViewModelBase
{
    public string Name { get; } = name;

    public object? Value { get; } = value;
}

public class TreeNode(TreeNode? parent, INode node) : ViewModelBase
{
    public INode Node { get; } = node;

    public string NodeName
    {
        get { return $"{Node.LocalName}"; }
    }

    string? _description;
    public string Description
    {
        get
        {
            if (_description == null)
            {
                var result = "";
                if (Node.Attributes.TryGetValue("Name", out var name))
                {
                    result = $"\"{name.Value}\"";
                }
                else if (Node.Attributes.TryGetValue("AutomationId", out var automationId))
                {
                    result = $"\"{automationId.Value}\"";
                }
                if (result == "\"\"")
                {
                    result = "";
                }
                _description = result;
            }
            return _description;
        }
    }

    public TreeNode? Parent { get; } = parent;

    ObservableCollection<TreeNode>? _children;
    public ObservableCollection<TreeNode> Children => _children ??= GetChildren();

    private ObservableCollection<TreeNode> GetChildren()
    {
        var children = new ObservableCollection<TreeNode>();

        foreach (var child in Node.Children)
        {
            children.Add(new TreeNode(this, child));
        }

        return children;
    }

    ObservableCollection<TreeNodeAttribute>? _attributes;
    public ObservableCollection<TreeNodeAttribute> Attributes => _attributes ??= GetAttributes();

    private ObservableCollection<TreeNodeAttribute> GetAttributes()
    {
        var children = new ObservableCollection<TreeNodeAttribute>();

        foreach (var child in Node.Attributes.Values)
        {
            children.Add(new TreeNodeAttribute(child.Name, child.Value));
        }

        return children;
    }

    private bool _isSelected;
    public bool IsSelected
    {
        get { return _isSelected; }
        set { this.RaiseAndSetIfChanged(ref _isSelected, value); }
    }

    private bool _isExpanded;
    public bool IsExpanded
    {
        get { return _isExpanded; }
        set { this.RaiseAndSetIfChanged(ref _isExpanded, value); }
    }

    public void Refresh()
    {
        Node.Invalidate();
        _children = null;
        _attributes = null;
        this.RaisePropertyChanged(nameof(Node));
        this.RaisePropertyChanged(nameof(NodeName));
        this.RaisePropertyChanged(nameof(Description));
        this.RaisePropertyChanged(nameof(Children));
        this.RaisePropertyChanged(nameof(Attributes));
    }

    public TreeNode? FindNode(INode node)
    {
        var result = FindNodeOnce(node);

        if (result != null)
        {
            return result;
        }

        Refresh();

        return FindNodeOnce(node);
    }

    public TreeNode? FindNodeOnce(INode node)
    {
        return Children.FirstOrDefault(x =>
        {
            if (x.Node.IsSamePosition(node))
            {
                return true;
            }
            return false;
        });
    }

    public IList<TreeNode> GetAncestors()
    {
        var result = new List<TreeNode>();

        var parent = Parent;
        while (parent != null)
        {
            result.Insert(0, parent);
            parent = parent.Parent;
        }

        return result;
    }
}
