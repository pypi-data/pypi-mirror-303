using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_setup_request_t
{
    [NativeTypeName("uint8_t")]
    public byte byte_order;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort protocol_major_version;

    [NativeTypeName("uint16_t")]
    public ushort protocol_minor_version;

    [NativeTypeName("uint16_t")]
    public ushort authorization_protocol_name_len;

    [NativeTypeName("uint16_t")]
    public ushort authorization_protocol_data_len;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
