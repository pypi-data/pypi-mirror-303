using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_format_t
{
    [NativeTypeName("uint8_t")]
    public byte depth;

    [NativeTypeName("uint8_t")]
    public byte bits_per_pixel;

    [NativeTypeName("uint8_t")]
    public byte scanline_pad;

    [NativeTypeName("uint8_t[5]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(5)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
