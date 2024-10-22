using System.Runtime.InteropServices;
using System.Security.Principal;

namespace PlatynUI.Provider.Core;

public static class UserInfo
{
    public static string GetUserId()
    {
        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
        {
            return GetWindowsUserId();
        }
        else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux) || RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
        {
            return GetUnixUserId().ToString();
        }
        else
        {
            throw new PlatformNotSupportedException("This method is only supported on Windows, Linux, and macOS.");
        }
    }

    private static string GetWindowsUserId()
    {
        return WindowsIdentity.GetCurrent().User?.Value ?? Environment.UserName;
    }

    private static uint GetUnixUserId()
    {
        return NativeMethods.getuid();
    }
}

internal static unsafe partial class NativeMethods
{
    [LibraryImport("libc")]
    internal static partial uint getuid();

    [LibraryImportAttribute("libc")]
    public static partial uint getgid();
}
