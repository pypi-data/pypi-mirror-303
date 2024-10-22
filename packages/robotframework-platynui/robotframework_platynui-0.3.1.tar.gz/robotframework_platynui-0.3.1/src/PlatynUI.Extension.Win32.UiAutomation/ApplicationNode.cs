// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.Diagnostics;
using PlatynUI.Runtime.Core;
using PlatynUI.Extension.Win32.UiAutomation.Core;

namespace PlatynUI.Extension.Win32.UiAutomation;

public class ApplicationNode(Runtime.Core.INode? parent, int processId) : Runtime.Core.INode
{
    public int ProcessId { get; } = processId;

    public Runtime.Core.INode? Parent { get; } = parent;

    private List<Runtime.Core.INode>? _children = null;
    public IList<Runtime.Core.INode> Children => _children ??= GetChildren();

    private List<Runtime.Core.INode> GetChildren()
    {
        var result = new List<Runtime.Core.INode>();
        foreach (var e in Automation.RootElement.EnumerateChildren(Automation.RawViewWalker, true))
        {
            if (e.CurrentProcessId != ProcessId)
            {
                continue;
            }
            result.Add(new ElementNode(this, e));
        }
        return result;
    }

    public string LocalName => "Application";

    public string NamespaceURI => Namespaces.App;

    private Dictionary<string, Runtime.Core.IAttribute>? _attributes;

    public IDictionary<string, Runtime.Core.IAttribute> Attributes => _attributes ??= GetAttributes();

    private Dictionary<string, Runtime.Core.IAttribute> GetAttributes()
    {
        var process = Process.GetProcessById(ProcessId);
        return new List<Runtime.Core.IAttribute>
        {
            new Runtime.Core.Attribute("Technology", "UIAutomation"),
            new Runtime.Core.Attribute("Name", process.ProcessName),
            new Runtime.Core.Attribute("ProcessId", process.Id),
            new Runtime.Core.Attribute("SessionId", process.SessionId),
            new Runtime.Core.Attribute("MainWindowHandle", process.MainWindowHandle),
            new Runtime.Core.Attribute("MainWindowTitle", process.MainWindowTitle),
            new Runtime.Core.Attribute("MainModule.FileName", process.MainModule?.FileName),
            new Runtime.Core.Attribute("MainModule.ModuleName", process.MainModule?.ModuleName),
            new Runtime.Core.Attribute(
                "FileVersionInfo.FileDescription",
                process.MainModule?.FileVersionInfo.FileDescription
            ),
            new Runtime.Core.Attribute("FileVersionInfo.ProductName", process.MainModule?.FileVersionInfo.ProductName),
            new Runtime.Core.Attribute(
                "FileVersionInfo.InternalName",
                process.MainModule?.FileVersionInfo.InternalName
            ),
            new Runtime.Core.Attribute("FileVersionInfo.CompanyName", process.MainModule?.FileVersionInfo.CompanyName),
            new Runtime.Core.Attribute("FileVersionInfo.Comments", process.MainModule?.FileVersionInfo.Comments),
            new Runtime.Core.Attribute("FileVersionInfo.FileVersion", process.MainModule?.FileVersionInfo.FileVersion),
            new Runtime.Core.Attribute(
                "FileVersionInfo.ProductVersion",
                process.MainModule?.FileVersionInfo.ProductVersion
            ),
            new Runtime.Core.Attribute(
                "FileVersionInfo.SpecialBuild",
                process.MainModule?.FileVersionInfo.SpecialBuild
            ),
            new Runtime.Core.Attribute("FileVersionInfo.IsDebug", process.MainModule?.FileVersionInfo.IsDebug)
        }
            .OrderBy(x => x.Name)
            .ToDictionary(a => a.Name);
    }

    public Runtime.Core.INode Clone()
    {
        return new ApplicationNode(Parent, ProcessId);
    }

    public bool IsSamePosition(Runtime.Core.INode other)
    {
        return other is ApplicationNode node && node.ProcessId == ProcessId;
    }

    public void Invalidate()
    {
        _attributes = null;
    }
}
