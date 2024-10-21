namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ewmh_wm_strut_partial_t
{
    [NativeTypeName("uint32_t")]
    public uint left;

    [NativeTypeName("uint32_t")]
    public uint right;

    [NativeTypeName("uint32_t")]
    public uint top;

    [NativeTypeName("uint32_t")]
    public uint bottom;

    [NativeTypeName("uint32_t")]
    public uint left_start_y;

    [NativeTypeName("uint32_t")]
    public uint left_end_y;

    [NativeTypeName("uint32_t")]
    public uint right_start_y;

    [NativeTypeName("uint32_t")]
    public uint right_end_y;

    [NativeTypeName("uint32_t")]
    public uint top_start_x;

    [NativeTypeName("uint32_t")]
    public uint top_end_x;

    [NativeTypeName("uint32_t")]
    public uint bottom_start_x;

    [NativeTypeName("uint32_t")]
    public uint bottom_end_x;
}
