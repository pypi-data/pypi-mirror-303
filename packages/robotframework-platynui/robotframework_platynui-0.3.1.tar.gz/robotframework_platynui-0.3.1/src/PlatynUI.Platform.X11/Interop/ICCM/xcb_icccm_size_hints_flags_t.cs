namespace PlatynUI.Platform.X11.Interop.XCB;

[NativeTypeName("unsigned int")]
public enum xcb_icccm_size_hints_flags_t : uint
{
    XCB_ICCCM_SIZE_HINT_US_POSITION = 1 << 0,
    XCB_ICCCM_SIZE_HINT_US_SIZE = 1 << 1,
    XCB_ICCCM_SIZE_HINT_P_POSITION = 1 << 2,
    XCB_ICCCM_SIZE_HINT_P_SIZE = 1 << 3,
    XCB_ICCCM_SIZE_HINT_P_MIN_SIZE = 1 << 4,
    XCB_ICCCM_SIZE_HINT_P_MAX_SIZE = 1 << 5,
    XCB_ICCCM_SIZE_HINT_P_RESIZE_INC = 1 << 6,
    XCB_ICCCM_SIZE_HINT_P_ASPECT = 1 << 7,
    XCB_ICCCM_SIZE_HINT_BASE_SIZE = 1 << 8,
    XCB_ICCCM_SIZE_HINT_P_WIN_GRAVITY = 1 << 9,
}
