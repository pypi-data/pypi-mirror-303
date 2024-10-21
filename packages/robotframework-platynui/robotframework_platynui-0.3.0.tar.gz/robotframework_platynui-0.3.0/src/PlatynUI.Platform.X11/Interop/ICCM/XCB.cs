using System.Runtime.InteropServices;
using static PlatynUI.Platform.X11.Interop.XCB.xcb_icccm_wm_t;

namespace PlatynUI.Platform.X11.Interop.XCB;

public static unsafe partial class XCB
{
    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_text_property(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_text_property_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_text_property_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_text_property_reply_t* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_get_text_property_reply_wipe(xcb_icccm_get_text_property_reply_t* prop);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_name_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_name(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_name(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_name_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_name_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_text_property_reply_t* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_icon_name_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_icon_name(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_icon_name(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_icon_name_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_icon_name_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_text_property_reply_t* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_colormap_windows_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_colormap_windows_atom, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("const xcb_window_t *")] uint* list);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_colormap_windows(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_colormap_windows_atom, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("const xcb_window_t *")] uint* list);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_colormap_windows(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_colormap_windows_atom);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_colormap_windows_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_colormap_windows_atom);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_colormap_windows_from_reply(xcb_get_property_reply_t* reply, xcb_icccm_get_wm_colormap_windows_reply_t* colormap_windows);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_colormap_windows_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_wm_colormap_windows_reply_t* windows, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_get_wm_colormap_windows_reply_wipe(xcb_icccm_get_wm_colormap_windows_reply_t* windows);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_client_machine_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_client_machine(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint encoding, [NativeTypeName("uint8_t")] byte format, [NativeTypeName("uint32_t")] uint name_len, [NativeTypeName("const char *")] sbyte* name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_client_machine(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_client_machine_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_client_machine_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_text_property_reply_t* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_class_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint class_len, [NativeTypeName("const char *")] sbyte* class_name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_class(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint class_len, [NativeTypeName("const char *")] sbyte* class_name);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_class(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_class_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_class_from_reply(xcb_icccm_get_wm_class_reply_t* prop, xcb_get_property_reply_t* reply);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_class_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_wm_class_reply_t* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_get_wm_class_reply_wipe(xcb_icccm_get_wm_class_reply_t* prop);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_transient_for_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_window_t")] uint transient_for_window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_transient_for(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_window_t")] uint transient_for_window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_transient_for(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_transient_for_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_transient_for_from_reply([NativeTypeName("xcb_window_t *")] uint* prop, xcb_get_property_reply_t* reply);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_transient_for_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, [NativeTypeName("xcb_window_t *")] uint* prop, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_position(xcb_size_hints_t* hints, int user_specified, [NativeTypeName("int32_t")] int x, [NativeTypeName("int32_t")] int y);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_size(xcb_size_hints_t* hints, int user_specified, [NativeTypeName("int32_t")] int width, [NativeTypeName("int32_t")] int height);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_min_size(xcb_size_hints_t* hints, [NativeTypeName("int32_t")] int min_width, [NativeTypeName("int32_t")] int min_height);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_max_size(xcb_size_hints_t* hints, [NativeTypeName("int32_t")] int max_width, [NativeTypeName("int32_t")] int max_height);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_resize_inc(xcb_size_hints_t* hints, [NativeTypeName("int32_t")] int width_inc, [NativeTypeName("int32_t")] int height_inc);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_aspect(xcb_size_hints_t* hints, [NativeTypeName("int32_t")] int min_aspect_num, [NativeTypeName("int32_t")] int min_aspect_den, [NativeTypeName("int32_t")] int max_aspect_num, [NativeTypeName("int32_t")] int max_aspect_den);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_base_size(xcb_size_hints_t* hints, [NativeTypeName("int32_t")] int base_width, [NativeTypeName("int32_t")] int base_height);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_size_hints_set_win_gravity(xcb_size_hints_t* hints, xcb_gravity_t win_gravity);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_size_hints_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property, xcb_size_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_size_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property, xcb_size_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_size_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_size_hints_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint property);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_size_hints_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_size_hints_t* hints, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_normal_hints_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, xcb_size_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_normal_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, xcb_size_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_normal_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_normal_hints_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_size_hints_from_reply(xcb_size_hints_t* hints, xcb_get_property_reply_t* reply);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_normal_hints_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_size_hints_t* hints, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint32_t")]
    public static extern uint xcb_icccm_wm_hints_get_urgency(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_input(xcb_icccm_wm_hints_t* hints, [NativeTypeName("uint8_t")] byte input);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_iconic(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_normal(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_withdrawn(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_none(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_icon_pixmap(xcb_icccm_wm_hints_t* hints, [NativeTypeName("xcb_pixmap_t")] uint icon_pixmap);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_icon_mask(xcb_icccm_wm_hints_t* hints, [NativeTypeName("xcb_pixmap_t")] uint icon_mask);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_icon_window(xcb_icccm_wm_hints_t* hints, [NativeTypeName("xcb_window_t")] uint icon_window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_window_group(xcb_icccm_wm_hints_t* hints, [NativeTypeName("xcb_window_t")] uint window_group);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_wm_hints_set_urgency(xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_hints_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, xcb_icccm_wm_hints_t* hints);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_hints(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_hints_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_hints_from_reply(xcb_icccm_wm_hints_t* hints, xcb_get_property_reply_t* reply);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_hints_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_wm_hints_t* hints, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_protocols_checked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_protocols, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_icccm_set_wm_protocols(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_protocols, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_protocols(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_protocol_atom);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_icccm_get_wm_protocols_unchecked(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_protocol_atom);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_protocols_from_reply(xcb_get_property_reply_t* reply, xcb_icccm_get_wm_protocols_reply_t* protocols);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_icccm_get_wm_protocols_reply(xcb_connection_t* c, xcb_get_property_cookie_t cookie, xcb_icccm_get_wm_protocols_reply_t* protocols, xcb_generic_error_t** e);

    [DllImport("xcb-util", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_icccm_get_wm_protocols_reply_wipe(xcb_icccm_get_wm_protocols_reply_t* protocols);

    [NativeTypeName("#define XCB_ICCCM_NUM_WM_SIZE_HINTS_ELEMENTS 18")]
    public const int XCB_ICCCM_NUM_WM_SIZE_HINTS_ELEMENTS = 18;

    [NativeTypeName("#define XCB_ICCCM_NUM_WM_HINTS_ELEMENTS 9")]
    public const int XCB_ICCCM_NUM_WM_HINTS_ELEMENTS = 9;

    [NativeTypeName("#define XCB_ICCCM_WM_ALL_HINTS (XCB_ICCCM_WM_HINT_INPUT | XCB_ICCCM_WM_HINT_STATE | \\\n                                XCB_ICCCM_WM_HINT_ICON_PIXMAP | XCB_ICCCM_WM_HINT_ICON_WINDOW | \\\n                                XCB_ICCCM_WM_HINT_ICON_POSITION | XCB_ICCCM_WM_HINT_ICON_MASK | \\\n                                XCB_ICCCM_WM_HINT_WINDOW_GROUP)")]
    public const int XCB_ICCCM_WM_ALL_HINTS = (int) (XCB_ICCCM_WM_HINT_INPUT | XCB_ICCCM_WM_HINT_STATE | XCB_ICCCM_WM_HINT_ICON_PIXMAP | XCB_ICCCM_WM_HINT_ICON_WINDOW | XCB_ICCCM_WM_HINT_ICON_POSITION | XCB_ICCCM_WM_HINT_ICON_MASK | XCB_ICCCM_WM_HINT_WINDOW_GROUP);
}
