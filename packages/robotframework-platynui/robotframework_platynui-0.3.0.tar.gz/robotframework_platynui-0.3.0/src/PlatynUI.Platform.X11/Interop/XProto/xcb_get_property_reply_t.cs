using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_get_property_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte format;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("xcb_atom_t")]
    public uint type;

    [NativeTypeName("uint32_t")]
    public uint bytes_after;

    [NativeTypeName("uint32_t")]
    public uint value_len;

    [NativeTypeName("uint8_t[12]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(12)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
