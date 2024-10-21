namespace PlatynUI.Provider.Core;

public static class PipeHelper
{
    public static string BuildPipeName(int id)
    {
        return $"Global\\PlatynUI.Provider_{UserInfo.GetUserId()}_{id}";
    }
}
