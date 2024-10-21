// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

using System.ComponentModel.Composition;
using System.Diagnostics;
using PlatynUI.Provider.Core;
using PlatynUI.Runtime;
using PlatynUI.Runtime.Core;

[assembly: PlatynUiExtension(supportedPlatforms: [RuntimePlatform.Any])]

namespace PlatynUI.Extension.Provider.Client;

[Export(typeof(INodeProvider))]
class NodeProvider : INodeProvider
{
    Dictionary<int, ProcessProvider> _providerProcesses = [];

    public IEnumerable<INode> GetNodes(INode parent)
    {
        ThreadHelper.JoinableTaskFactory.Run(async () =>
        {
            var tasks = new List<Task<ProcessProvider?>>();
            foreach (var process in Process.GetProcesses())
            {
                if (_providerProcesses.ContainsKey(process.Id))
                {
                    continue;
                }

                var pipeName = PipeHelper.BuildPipeName(process.Id);

                if (Mutex.TryOpenExisting(pipeName, out var mutex))
                {
                    Debug.WriteLine($"Found mutex for process {process.Id} with name {process.ProcessName}");
                }
                else
                {
                    continue;
                }

                process.EnableRaisingEvents = true;

                process.Exited += (sender, e) =>
                {
                    if (_providerProcesses.TryGetValue(process.Id, out ProcessProvider? value))
                    {
                        value.Dispose();
                        _providerProcesses.Remove(process.Id);
                    }
                };
                tasks.Add(
                    Task.Run(async () =>
                    {
                        var provider = new ProcessProvider(process, pipeName, parent);
                        try
                        {
                            await provider.ConnectAsync();
                            return provider;
                        }
                        catch
                        {
                            provider.Dispose();
                            return null;
                        }
                    })
                );
            }
            var connected = (await Task.WhenAll(tasks) ?? []).Where(x => x != null);
            foreach (var provider in connected)
            {
                if (provider != null)
                {
                    _providerProcesses[provider.Process.Id] = provider;
                }
            }
        });

        return _providerProcesses.Values.Select(x => x.GetRootNode()).Where(x => x != null).Cast<INode>().ToList();
    }
}
