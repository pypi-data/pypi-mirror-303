using System;
using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.ReactiveUI;
using PlatynUI.Provider.Avalonia;

namespace AvaloniaTestApp;

sealed class Program
{
    // Initialization code. Don't use any Avalonia, third-party APIs or any
    // SynchronizationContext-reliant code before AppMain is called: things aren't initialized
    // yet and stuff might break.
    [STAThread]
    public static void Main(string[] args)
    {
        BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);
    }

    // static void BuildLifeTime(IClassicDesktopStyleApplicationLifetime lifetime)
    // {
    //     PlatynUI.Provider.Avalonia.Server.Start(lifetime);

    //     lifetime.Exit += (sender, e) => PlatynUI.Provider.Avalonia.Server.Stop();
    // }

    // Avalonia configuration, don't remove; also used by visual designer.
    public static AppBuilder BuildAvaloniaApp() =>
        AppBuilder
            .Configure<App>()
            .UsePlatformDetect()
            .WithInterFont()
            .LogToTrace()
            .UseReactiveUI()
            .EnablePlatynUIServer();
}
