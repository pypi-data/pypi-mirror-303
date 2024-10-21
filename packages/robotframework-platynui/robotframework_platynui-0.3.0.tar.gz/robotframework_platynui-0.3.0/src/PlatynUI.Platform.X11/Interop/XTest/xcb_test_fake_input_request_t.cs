using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_test_fake_input_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte minor_opcode;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("uint8_t")]
    public byte type;

    [NativeTypeName("uint8_t")]
    public byte detail;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [NativeTypeName("uint32_t")]
    public uint time;

    [NativeTypeName("xcb_window_t")]
    public uint root;

    [NativeTypeName("uint8_t[8]")]
    public _pad1_e__FixedBuffer pad1;

    [NativeTypeName("int16_t")]
    public short rootX;

    [NativeTypeName("int16_t")]
    public short rootY;

    [NativeTypeName("uint8_t[7]")]
    public _pad2_e__FixedBuffer pad2;

    [NativeTypeName("uint8_t")]
    public byte deviceid;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(8)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(7)]
    public partial struct _pad2_e__FixedBuffer
    {
        public byte e0;
    }
}
