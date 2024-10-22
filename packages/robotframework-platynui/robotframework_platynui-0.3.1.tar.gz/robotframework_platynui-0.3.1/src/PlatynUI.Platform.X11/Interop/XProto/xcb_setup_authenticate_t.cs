using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_setup_authenticate_t
{
    [NativeTypeName("uint8_t")]
    public byte status;

    [NativeTypeName("uint8_t[5]")]
    public _pad0_e__FixedBuffer pad0;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [InlineArray(5)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
