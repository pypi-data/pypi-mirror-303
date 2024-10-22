namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_wm_icon_iterator_t
{
    [NativeTypeName("uint32_t")]
    public uint width;

    [NativeTypeName("uint32_t")]
    public uint height;

    [NativeTypeName("uint32_t *")]
    public uint* data;

    [NativeTypeName("unsigned int")]
    public uint rem;

    [NativeTypeName("unsigned int")]
    public uint index;
}
