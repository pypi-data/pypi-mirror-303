namespace PlatynUI.Platform.X11.Interop.XCB;

[NativeTypeName("unsigned int")]
public enum xcb_icccm_wm_t : uint
{
    XCB_ICCCM_WM_HINT_INPUT = (1 << 0),
    XCB_ICCCM_WM_HINT_STATE = (1 << 1),
    XCB_ICCCM_WM_HINT_ICON_PIXMAP = (1 << 2),
    XCB_ICCCM_WM_HINT_ICON_WINDOW = (1 << 3),
    XCB_ICCCM_WM_HINT_ICON_POSITION = (1 << 4),
    XCB_ICCCM_WM_HINT_ICON_MASK = (1 << 5),
    XCB_ICCCM_WM_HINT_WINDOW_GROUP = (1 << 6),
    XCB_ICCCM_WM_HINT_X_URGENCY = (1 << 8),
}
