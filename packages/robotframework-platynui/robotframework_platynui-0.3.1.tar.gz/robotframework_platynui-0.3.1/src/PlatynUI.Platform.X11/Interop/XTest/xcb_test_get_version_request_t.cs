namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_test_get_version_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte minor_opcode;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("uint8_t")]
    public byte major_version;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort minor_version;
}
