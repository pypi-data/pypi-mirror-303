namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_get_utf8_strings_reply_t
{
    [NativeTypeName("uint32_t")]
    public uint strings_len;

    [NativeTypeName("char *")]
    public sbyte* strings;

    public xcb_get_property_reply_t* _reply;
}
