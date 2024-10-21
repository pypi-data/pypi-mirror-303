using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

[StructLayout(LayoutKind.Explicit)]
public partial struct xcb_client_message_data_t
{
    [FieldOffset(0)]
    [NativeTypeName("uint8_t[20]")]
    public _data8_e__FixedBuffer data8;

    [FieldOffset(0)]
    [NativeTypeName("uint16_t[10]")]
    public _data16_e__FixedBuffer data16;

    [FieldOffset(0)]
    [NativeTypeName("uint32_t[5]")]
    public _data32_e__FixedBuffer data32;

    [InlineArray(20)]
    public partial struct _data8_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(10)]
    public partial struct _data16_e__FixedBuffer
    {
        public ushort e0;
    }

    [InlineArray(5)]
    public partial struct _data32_e__FixedBuffer
    {
        public uint e0;
    }
}
