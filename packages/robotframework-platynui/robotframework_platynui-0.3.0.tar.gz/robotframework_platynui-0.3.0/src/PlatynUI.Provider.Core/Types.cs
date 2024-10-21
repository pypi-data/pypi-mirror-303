namespace PlatynUI.Provider.Core
{
    public readonly struct ElementReference(int[] runtimeId)
    {
        public readonly int[] RuntimeId = runtimeId;

        public override readonly string ToString()
        {
            return $"NodeReference(RuntimeId: {string.Join(", ", RuntimeId)})";
        }

        public static bool operator ==(ElementReference left, ElementReference right)
        {
            return left.RuntimeId.SequenceEqual(right.RuntimeId);
        }

        public static bool operator !=(ElementReference left, ElementReference right)
        {
            return !left.RuntimeId.SequenceEqual(right.RuntimeId);
        }

        public override readonly bool Equals(object? obj)
        {
            return obj is ElementReference reference && this == reference;
        }

        public override readonly int GetHashCode()
        {
            return HashCode.Combine(RuntimeId);
        }
    }

    public interface IApplicationInfoAsync
    {
        Task<ElementReference?> GetRootAsync();
    }

    public enum NodeType
    {
        Unknown,
        Element,
        Application,
        Item,
    }

    public interface INodeInfoAsync
    {
        Task<bool> IsValidAsync(ElementReference reference);

        Task<string> GetLocalNameAsync(ElementReference reference);
        Task<NodeType> GetNodeTypeAsync(ElementReference reference);
        Task<IList<ElementReference>> GetChildrenAsync(ElementReference parentReference);
        Task<string[]> GetAttributeNamesAsync(ElementReference reference);
        Task<object?> GetAttributeValueAsync(ElementReference reference, string attributeName);
        Task<string> GetAttributeTypeAsync(ElementReference reference, string attributeName);
    }
}
