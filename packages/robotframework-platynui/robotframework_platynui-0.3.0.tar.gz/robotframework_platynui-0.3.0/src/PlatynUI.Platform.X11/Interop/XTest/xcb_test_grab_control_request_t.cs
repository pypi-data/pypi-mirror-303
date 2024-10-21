using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_test_grab_control_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte minor_opcode;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("uint8_t")]
    public byte impervious;

    [NativeTypeName("uint8_t[3]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(3)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
