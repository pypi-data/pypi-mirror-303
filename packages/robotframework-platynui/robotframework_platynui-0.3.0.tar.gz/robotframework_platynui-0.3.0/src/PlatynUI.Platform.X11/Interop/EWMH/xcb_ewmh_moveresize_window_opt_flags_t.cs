namespace PlatynUI.Platform.X11.Interop.XCB;

[NativeTypeName("unsigned int")]
public enum xcb_ewmh_moveresize_window_opt_flags_t : uint
{
    XCB_EWMH_MOVERESIZE_WINDOW_X = (1 << 8),
    XCB_EWMH_MOVERESIZE_WINDOW_Y = (1 << 9),
    XCB_EWMH_MOVERESIZE_WINDOW_WIDTH = (1 << 10),
    XCB_EWMH_MOVERESIZE_WINDOW_HEIGHT = (1 << 11),
}
