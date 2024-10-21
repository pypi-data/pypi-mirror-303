namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_get_desktop_viewport_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint desktop_viewport_len;

    public xcb_ewmh_coordinates_t* desktop_viewport;

    public xcb_get_property_reply_t* _reply;
}
