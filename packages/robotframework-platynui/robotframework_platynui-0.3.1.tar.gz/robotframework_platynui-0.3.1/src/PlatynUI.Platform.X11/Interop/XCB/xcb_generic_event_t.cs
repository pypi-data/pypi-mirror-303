using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_generic_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t[7]")]
    public _pad_e__FixedBuffer pad;

    [NativeTypeName("uint32_t")]
    public uint full_sequence;

    [InlineArray(7)]
    public partial struct _pad_e__FixedBuffer
    {
        public uint e0;
    }
}
