using System;
using ReactiveUI;

namespace AvaloniaTestApp.ViewModels;

public class MainWindowViewModel : ViewModelBase
{
    private string _greeting = "Welcome to Avalonia!";
    public string Greeting
    {
        get => _greeting;
        set
        {
            if (value.Contains("hi"))
                throw new ArgumentException("No hi allowed");
            this.RaiseAndSetIfChanged(ref _greeting, value);
        }
    }

    public void ClickCommand()
    {
        Greeting = "Hello Avalonia!";
    }
}
