using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_list_extensions_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte names_len;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("uint8_t[24]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(24)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
