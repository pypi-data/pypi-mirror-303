namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_ewmh_coordinates_t
{
    [NativeTypeName("uint32_t")]
    public uint x;

    [NativeTypeName("uint32_t")]
    public uint y;
}
