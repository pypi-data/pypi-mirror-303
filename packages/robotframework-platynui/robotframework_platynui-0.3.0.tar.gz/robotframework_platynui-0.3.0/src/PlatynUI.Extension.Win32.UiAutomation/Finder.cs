// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Diagnostics;
using System.Xml.XPath;
using PlatynUI.Extension.Win32.UiAutomation.Client;
using PlatynUI.Extension.Win32.UiAutomation.Core;

namespace PlatynUI.Extension.Win32.UiAutomation;

public static class Finder
{
    static readonly XsltContext xsltContext = new();

    public static IUIAutomationElement? FindSingleElement(
        IUIAutomationElement? parent,
        string xpath,
        bool findVirtual = false
    )
    {
        var stopwatch = Stopwatch.StartNew();

        var navigator = new Core.XPathNavigator(parent, findVirtual, xsltContext.NameTable);
        var expression = XPathExpression.Compile(xpath, xsltContext);

        var node = navigator.SelectSingleNode(expression);
        Debug.WriteLine($"XPath '{xpath}' search took {stopwatch.ElapsedMilliseconds}ms");

        return node?.UnderlyingObject as IUIAutomationElement;
    }

    public static List<IUIAutomationElement> FindAllElements(
        IUIAutomationElement? parent,
        string xpath,
        bool findVirtual = false
    )
    {
        var stopwatch = Stopwatch.StartNew();

        var navigator = new Core.XPathNavigator(parent, findVirtual);
        var expression = XPathExpression.Compile(xpath, xsltContext);

        var nodes = navigator.Select(expression);
        Debug.WriteLine($"XPath '{xpath}' search took {stopwatch.ElapsedMilliseconds}ms");

        var result = new List<IUIAutomationElement>();
        while (nodes.MoveNext())
        {
            if (nodes.Current is System.Xml.XPath.XPathNavigator node)
            {
                if (node?.UnderlyingObject is IUIAutomationElement element)
                    result.Add(element);
            }
        }
        return result;
    }

    public static IEnumerable<IUIAutomationElement> EnumAllElements(
        IUIAutomationElement? parent,
        string xpath,
        bool findVirtual = false
    )
    {
        var stopwatch = Stopwatch.StartNew();

        var navigator = new Core.XPathNavigator(parent, findVirtual);
        var expression = XPathExpression.Compile(xpath, xsltContext);

        var nodes = navigator.Select(expression);

        while (nodes.MoveNext())
        {
            if (nodes.Current is System.Xml.XPath.XPathNavigator node)
            {
                if (node?.UnderlyingObject is IUIAutomationElement element)
                    yield return element;
            }
        }
    }

    public static List<object?> Evaluate(IUIAutomationElement? parent, string xpath, bool findVirtual = false)
    {
        var stopwatch = Stopwatch.StartNew();

        var navigator = new Core.XPathNavigator(parent, findVirtual);
        var expression = XPathExpression.Compile(xpath, xsltContext);

        var nodes = navigator.Evaluate(expression);
        Debug.WriteLine($"XPath '{xpath}' search took {stopwatch.ElapsedMilliseconds}ms");

        var result = new List<object?>();
        if (nodes is XPathNodeIterator iterator)
            while (iterator!.MoveNext())
            {
                if (iterator.Current is System.Xml.XPath.XPathNavigator node)
                {
                    if (node?.UnderlyingObject is IUIAutomationElement element)
                        result.Add(element);
                    else
                        result.Add(node?.TypedValue);
                }
                else
                {
                    result.Add(iterator!.Current!.TypedValue);
                }
            }
        else
        {
            result.Add(nodes);
        }
        return result;
    }
}
