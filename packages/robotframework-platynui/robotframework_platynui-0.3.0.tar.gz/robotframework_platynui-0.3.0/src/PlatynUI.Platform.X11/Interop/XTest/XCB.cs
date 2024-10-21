using System.Runtime.InteropServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public static unsafe partial class XCB
{
    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_get_version_cookie_t xcb_test_get_version(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte major_version, [NativeTypeName("uint16_t")] ushort minor_version);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_get_version_cookie_t xcb_test_get_version_unchecked(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte major_version, [NativeTypeName("uint16_t")] ushort minor_version);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_get_version_reply_t* xcb_test_get_version_reply(xcb_connection_t* c, xcb_test_get_version_cookie_t cookie, xcb_generic_error_t** e);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_compare_cursor_cookie_t xcb_test_compare_cursor(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_cursor_t")] uint cursor);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_compare_cursor_cookie_t xcb_test_compare_cursor_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_cursor_t")] uint cursor);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_test_compare_cursor_reply_t* xcb_test_compare_cursor_reply(xcb_connection_t* c, xcb_test_compare_cursor_cookie_t cookie, xcb_generic_error_t** e);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_test_fake_input_checked(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte type, [NativeTypeName("uint8_t")] byte detail, [NativeTypeName("uint32_t")] uint time, [NativeTypeName("xcb_window_t")] uint root, [NativeTypeName("int16_t")] short rootX, [NativeTypeName("int16_t")] short rootY, [NativeTypeName("uint8_t")] byte deviceid);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_test_fake_input(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte type, [NativeTypeName("uint8_t")] byte detail, [NativeTypeName("uint32_t")] uint time, [NativeTypeName("xcb_window_t")] uint root, [NativeTypeName("int16_t")] short rootX, [NativeTypeName("int16_t")] short rootY, [NativeTypeName("uint8_t")] byte deviceid);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_test_grab_control_checked(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte impervious);

    [DllImport("xcb-xtest", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_test_grab_control(xcb_connection_t* c, [NativeTypeName("uint8_t")] byte impervious);

    [NativeTypeName("#define XCB_TEST_MAJOR_VERSION 2")]
    public const int XCB_TEST_MAJOR_VERSION = 2;

    [NativeTypeName("#define XCB_TEST_MINOR_VERSION 2")]
    public const int XCB_TEST_MINOR_VERSION = 2;

    [NativeTypeName("#define XCB_TEST_GET_VERSION 0")]
    public const int XCB_TEST_GET_VERSION = 0;

    [NativeTypeName("#define XCB_TEST_COMPARE_CURSOR 1")]
    public const int XCB_TEST_COMPARE_CURSOR = 1;

    [NativeTypeName("#define XCB_TEST_FAKE_INPUT 2")]
    public const int XCB_TEST_FAKE_INPUT = 2;

    [NativeTypeName("#define XCB_TEST_GRAB_CONTROL 3")]
    public const int XCB_TEST_GRAB_CONTROL = 3;
}
