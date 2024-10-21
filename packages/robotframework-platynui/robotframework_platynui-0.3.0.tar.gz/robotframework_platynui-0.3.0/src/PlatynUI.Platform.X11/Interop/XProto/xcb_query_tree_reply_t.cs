using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_query_tree_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("xcb_window_t")]
    public uint root;

    [NativeTypeName("xcb_window_t")]
    public uint parent;

    [NativeTypeName("uint16_t")]
    public ushort children_len;

    [NativeTypeName("uint8_t[14]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(14)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
