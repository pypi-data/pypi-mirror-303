namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ewmh_get_desktop_layout_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint orientation;

    [NativeTypeName("uint32_t")]
    public uint columns;

    [NativeTypeName("uint32_t")]
    public uint rows;

    [NativeTypeName("uint32_t")]
    public uint starting_corner;
}
