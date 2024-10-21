// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;
using PlatynUI.Runtime;
using PlatynUI.Runtime.Core;
using PlatynUI.Extension.Win32.UiAutomation.Core;

[assembly: PlatynUiExtension(supportedPlatforms: [RuntimePlatform.Windows])]

namespace PlatynUI.Extension.Win32.UiAutomation;

[Export(typeof(INodeProvider))]
class NodeProvider : INodeProvider
{
    public IEnumerable<Runtime.Core.INode> GetNodes(Runtime.Core.INode parent)
    {
        var processIds = new HashSet<int>();

        foreach (var e in Automation.RootElement.EnumerateChildren(Automation.RawViewWalker, true))
        {
            processIds.Add(e.CurrentProcessId);
            yield return new ElementNode(parent, e);
        }

        foreach (var processId in processIds)
        {
            yield return new ApplicationNode(parent, processId);
        }
    }
}
