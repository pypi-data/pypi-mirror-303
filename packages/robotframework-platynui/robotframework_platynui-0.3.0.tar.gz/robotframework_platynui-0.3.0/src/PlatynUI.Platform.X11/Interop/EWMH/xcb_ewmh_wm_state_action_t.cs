namespace PlatynUI.Platform.X11.Interop.XCB;

[NativeTypeName("unsigned int")]
public enum xcb_ewmh_wm_state_action_t : uint
{
    XCB_EWMH_WM_STATE_REMOVE = 0,
    XCB_EWMH_WM_STATE_ADD = 1,
    XCB_EWMH_WM_STATE_TOGGLE = 2,
}
