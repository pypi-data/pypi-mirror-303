using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_alloc_color_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_colormap_t")]
    public uint cmap;

    [NativeTypeName("uint16_t")]
    public ushort red;

    [NativeTypeName("uint16_t")]
    public ushort green;

    [NativeTypeName("uint16_t")]
    public ushort blue;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
