namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_icccm_get_wm_class_reply_t
{
    [NativeTypeName("char *")]
    public sbyte* instance_name;

    [NativeTypeName("char *")]
    public sbyte* class_name;

    public xcb_get_property_reply_t* _reply;
}
