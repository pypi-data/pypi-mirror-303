namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_get_wm_icon_reply_t
{
    [NativeTypeName("unsigned int")]
    public uint num_icons;

    public xcb_get_property_reply_t* _reply;
}
