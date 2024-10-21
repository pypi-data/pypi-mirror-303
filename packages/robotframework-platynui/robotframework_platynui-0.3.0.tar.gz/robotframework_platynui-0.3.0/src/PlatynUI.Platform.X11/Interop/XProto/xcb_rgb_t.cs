using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_rgb_t
{
    [NativeTypeName("uint16_t")]
    public ushort red;

    [NativeTypeName("uint16_t")]
    public ushort green;

    [NativeTypeName("uint16_t")]
    public ushort blue;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
