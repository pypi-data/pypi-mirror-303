using Microsoft.VisualStudio.Threading;

using PlatynUI.Provider.Server;

namespace PlatynUI.Provider.Avalonia;

public static class Server
{
    static readonly JoinableTaskContext JoinableTaskContext = new();
    static readonly JoinableTaskFactory JoinableTaskFactory = new(JoinableTaskContext);

    public static void Start()
    {
        new Thread(() =>
        {
            JoinableTaskFactory.Run(() => RunAsync());
        }).Start();
    }

    public static void Stop()
    {
        cts.Cancel();
    }

    private static readonly CancellationTokenSource cts = new();

    public static async Task RunAsync()
    {
        var server = new ProviderServer(new ApplicationInfo(), new NodeInfo());

        await server.RunAsync(cts.Token);
    }
}
