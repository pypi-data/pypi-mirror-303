namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_icccm_wm_hints_t
{
    [NativeTypeName("int32_t")]
    public int flags;

    [NativeTypeName("uint32_t")]
    public uint input;

    [NativeTypeName("int32_t")]
    public int initial_state;

    [NativeTypeName("xcb_pixmap_t")]
    public uint icon_pixmap;

    [NativeTypeName("xcb_window_t")]
    public uint icon_window;

    [NativeTypeName("int32_t")]
    public int icon_x;

    [NativeTypeName("int32_t")]
    public int icon_y;

    [NativeTypeName("xcb_pixmap_t")]
    public uint icon_mask;

    [NativeTypeName("xcb_window_t")]
    public uint window_group;
}
