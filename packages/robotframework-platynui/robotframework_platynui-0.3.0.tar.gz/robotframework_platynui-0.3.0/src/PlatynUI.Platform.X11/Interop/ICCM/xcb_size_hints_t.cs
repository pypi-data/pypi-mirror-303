namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_size_hints_t
{
    [NativeTypeName("uint32_t")]
    public uint flags;

    [NativeTypeName("int32_t")]
    public int x;

    [NativeTypeName("int32_t")]
    public int y;

    [NativeTypeName("int32_t")]
    public int width;

    [NativeTypeName("int32_t")]
    public int height;

    [NativeTypeName("int32_t")]
    public int min_width;

    [NativeTypeName("int32_t")]
    public int min_height;

    [NativeTypeName("int32_t")]
    public int max_width;

    [NativeTypeName("int32_t")]
    public int max_height;

    [NativeTypeName("int32_t")]
    public int width_inc;

    [NativeTypeName("int32_t")]
    public int height_inc;

    [NativeTypeName("int32_t")]
    public int min_aspect_num;

    [NativeTypeName("int32_t")]
    public int min_aspect_den;

    [NativeTypeName("int32_t")]
    public int max_aspect_num;

    [NativeTypeName("int32_t")]
    public int max_aspect_den;

    [NativeTypeName("int32_t")]
    public int base_width;

    [NativeTypeName("int32_t")]
    public int base_height;

    [NativeTypeName("uint32_t")]
    public uint win_gravity;
}
