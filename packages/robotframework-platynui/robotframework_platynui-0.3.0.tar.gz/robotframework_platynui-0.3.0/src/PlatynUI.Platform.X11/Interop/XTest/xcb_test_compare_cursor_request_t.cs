namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_test_compare_cursor_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte minor_opcode;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_window_t")]
    public uint window;

    [NativeTypeName("xcb_cursor_t")]
    public uint cursor;
}
