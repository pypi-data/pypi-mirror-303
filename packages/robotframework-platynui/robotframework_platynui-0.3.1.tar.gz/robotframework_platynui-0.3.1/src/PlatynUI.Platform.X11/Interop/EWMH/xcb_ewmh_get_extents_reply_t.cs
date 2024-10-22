namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ewmh_get_extents_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint left;

    [NativeTypeName("uint32_t")]
    public uint right;

    [NativeTypeName("uint32_t")]
    public uint top;

    [NativeTypeName("uint32_t")]
    public uint bottom;
}
