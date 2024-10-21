using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_depth_t
{
    [NativeTypeName("uint8_t")]
    public byte depth;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort visuals_len;

    [NativeTypeName("uint8_t[4]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(4)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
