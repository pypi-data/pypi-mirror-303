using PlatynUI.Provider.Core;

namespace PlatynUI.Provider.Avalonia;

public class ApplicationInfo : IApplicationInfoAsync
{
    public Task<ElementReference?> GetRootAsync()
    {
        return Task.FromResult<ElementReference?>(NodeInfo.GetOrCreateNode<ApplicationNode>().Reference);
    }
}
