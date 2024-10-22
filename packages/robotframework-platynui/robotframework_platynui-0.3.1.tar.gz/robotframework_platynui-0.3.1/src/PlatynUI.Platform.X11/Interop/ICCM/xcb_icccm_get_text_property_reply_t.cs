namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_icccm_get_text_property_reply_t
{
    public xcb_get_property_reply_t* _reply;

    [NativeTypeName("xcb_atom_t")]
    public uint encoding;

    [NativeTypeName("uint32_t")]
    public uint name_len;

    [NativeTypeName("char *")]
    public sbyte* name;

    [NativeTypeName("uint8_t")]
    public byte format;
}
