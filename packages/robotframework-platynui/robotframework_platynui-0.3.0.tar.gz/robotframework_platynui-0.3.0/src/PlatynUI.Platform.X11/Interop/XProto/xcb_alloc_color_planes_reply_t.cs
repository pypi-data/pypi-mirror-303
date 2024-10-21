using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_alloc_color_planes_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("uint16_t")]
    public ushort pixels_len;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [NativeTypeName("uint32_t")]
    public uint red_mask;

    [NativeTypeName("uint32_t")]
    public uint green_mask;

    [NativeTypeName("uint32_t")]
    public uint blue_mask;

    [NativeTypeName("uint8_t[8]")]
    public _pad2_e__FixedBuffer pad2;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(8)]
    public partial struct _pad2_e__FixedBuffer
    {
        public byte e0;
    }
}
