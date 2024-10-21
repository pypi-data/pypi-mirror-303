namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_get_workarea_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint workarea_len;

    public xcb_ewmh_geometry_t* workarea;

    public xcb_get_property_reply_t* _reply;
}
