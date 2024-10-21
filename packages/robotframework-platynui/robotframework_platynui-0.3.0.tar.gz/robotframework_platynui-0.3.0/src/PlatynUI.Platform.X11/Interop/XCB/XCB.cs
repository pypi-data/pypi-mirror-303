using System.Runtime.InteropServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public static unsafe partial class XCB
{
    [NativeTypeName("#define X_PROTOCOL 11")]
    public const int X_PROTOCOL = 11;

    [NativeTypeName("#define X_PROTOCOL_REVISION 0")]
    public const int X_PROTOCOL_REVISION = 0;

    [NativeTypeName("#define X_TCP_PORT 6000")]
    public const int X_TCP_PORT = 6000;

    [NativeTypeName("#define XCB_CONN_ERROR 1")]
    public const int XCB_CONN_ERROR = 1;

    [NativeTypeName("#define XCB_CONN_CLOSED_EXT_NOTSUPPORTED 2")]
    public const int XCB_CONN_CLOSED_EXT_NOTSUPPORTED = 2;

    [NativeTypeName("#define XCB_CONN_CLOSED_MEM_INSUFFICIENT 3")]
    public const int XCB_CONN_CLOSED_MEM_INSUFFICIENT = 3;

    [NativeTypeName("#define XCB_CONN_CLOSED_REQ_LEN_EXCEED 4")]
    public const int XCB_CONN_CLOSED_REQ_LEN_EXCEED = 4;

    [NativeTypeName("#define XCB_CONN_CLOSED_PARSE_ERR 5")]
    public const int XCB_CONN_CLOSED_PARSE_ERR = 5;

    [NativeTypeName("#define XCB_CONN_CLOSED_INVALID_SCREEN 6")]
    public const int XCB_CONN_CLOSED_INVALID_SCREEN = 6;

    [NativeTypeName("#define XCB_CONN_CLOSED_FDPASSING_FAILED 7")]
    public const int XCB_CONN_CLOSED_FDPASSING_FAILED = 7;

    [NativeTypeName("#define XCB_NONE 0L")]
    public const nint XCB_NONE = 0;

    [NativeTypeName("#define XCB_COPY_FROM_PARENT 0L")]
    public const nint XCB_COPY_FROM_PARENT = 0;

    [NativeTypeName("#define XCB_CURRENT_TIME 0L")]
    public const nint XCB_CURRENT_TIME = 0;

    [NativeTypeName("#define XCB_NO_SYMBOL 0L")]
    public const nint XCB_NO_SYMBOL = 0;

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern int xcb_flush(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint32_t")]
    public static extern uint xcb_get_maximum_request_length(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_prefetch_maximum_request_length(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_event_t* xcb_wait_for_event(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_event_t* xcb_poll_for_event(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_event_t* xcb_poll_for_queued_event(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_event_t* xcb_poll_for_special_event(xcb_connection_t* c, [NativeTypeName("xcb_special_event_t *")] xcb_special_event* se);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_event_t* xcb_wait_for_special_event(xcb_connection_t* c, [NativeTypeName("xcb_special_event_t *")] xcb_special_event* se);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("xcb_special_event_t *")]
    public static extern xcb_special_event* xcb_register_for_special_xge(xcb_connection_t* c, xcb_extension_t* ext, [NativeTypeName("uint32_t")] uint eid, [NativeTypeName("uint32_t *")] uint* stamp);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_unregister_for_special_event(xcb_connection_t* c, [NativeTypeName("xcb_special_event_t *")] xcb_special_event* se);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_generic_error_t* xcb_request_check(xcb_connection_t* c, xcb_void_cookie_t cookie);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_discard_reply(xcb_connection_t* c, [NativeTypeName("unsigned int")] uint sequence);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_discard_reply64(xcb_connection_t* c, [NativeTypeName("uint64_t")] nuint sequence);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("const struct xcb_query_extension_reply_t *")]
    public static extern xcb_query_extension_reply_t* xcb_get_extension_data(xcb_connection_t* c, xcb_extension_t* ext);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_prefetch_extension_data(xcb_connection_t* c, xcb_extension_t* ext);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("const struct xcb_setup_t *")]
    public static extern xcb_setup_t* xcb_get_setup(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern int xcb_get_file_descriptor(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern int xcb_connection_has_error(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_connection_t* xcb_connect_to_fd(int fd, xcb_auth_info_t* auth_info);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_disconnect(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern int xcb_parse_display([NativeTypeName("const char *")] sbyte* name, [NativeTypeName("char **")] sbyte** host, int* display, int* screen);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_connection_t* xcb_connect([NativeTypeName("const char *")] sbyte* displayname, int* screenp);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_connection_t* xcb_connect_to_display_with_auth_info([NativeTypeName("const char *")] sbyte* display, xcb_auth_info_t* auth, int* screen);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint32_t")]
    public static extern uint xcb_generate_id(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint64_t")]
    public static extern nuint xcb_total_read(xcb_connection_t* c);

    [DllImport("xcb", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint64_t")]
    public static extern nuint xcb_total_written(xcb_connection_t* c);
}
