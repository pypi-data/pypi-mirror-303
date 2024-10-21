namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ewmh_get_wm_fullscreen_monitors_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint top;

    [NativeTypeName("uint32_t")]
    public uint bottom;

    [NativeTypeName("uint32_t")]
    public uint left;

    [NativeTypeName("uint32_t")]
    public uint right;
}
