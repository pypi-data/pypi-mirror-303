namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_test_compare_cursor_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte same;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;
}
