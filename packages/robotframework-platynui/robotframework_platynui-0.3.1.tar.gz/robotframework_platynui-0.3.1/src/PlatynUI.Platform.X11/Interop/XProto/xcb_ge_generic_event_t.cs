using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ge_generic_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte extension;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("uint16_t")]
    public ushort event_type;

    [NativeTypeName("uint8_t[22]")]
    public _pad0_e__FixedBuffer pad0;

    [NativeTypeName("uint32_t")]
    public uint full_sequence;

    [InlineArray(22)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
