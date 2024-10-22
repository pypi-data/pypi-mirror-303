using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_generic_error_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte error_code;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint resource_id;

    [NativeTypeName("uint16_t")]
    public ushort minor_code;

    [NativeTypeName("uint8_t")]
    public byte major_code;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint32_t[5]")]
    public _pad_e__FixedBuffer pad;

    [NativeTypeName("uint32_t")]
    public uint full_sequence;

    [InlineArray(5)]
    public partial struct _pad_e__FixedBuffer
    {
        public uint e0;
    }
}
