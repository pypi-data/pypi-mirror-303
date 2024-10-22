using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_fill_poly_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_drawable_t")]
    public uint drawable;

    [NativeTypeName("xcb_gcontext_t")]
    public uint gc;

    [NativeTypeName("uint8_t")]
    public byte shape;

    [NativeTypeName("uint8_t")]
    public byte coordinate_mode;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
