using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;

namespace PlatynUI.Provider.Avalonia;

public static class AppBuilderExtensions
{
    public static AppBuilder EnablePlatynUIServer(this AppBuilder builder)
    {
        return builder.AfterSetup(_ =>
        {
            StartServer();
        });
    }

    public static void StartServer()
    {
        if (Application.Current?.ApplicationLifetime is IClassicDesktopStyleApplicationLifetime lifetime)
        {
            lifetime.Exit += (sender, e) => Server.Stop();
            Server.Start();
        }
    }
}
