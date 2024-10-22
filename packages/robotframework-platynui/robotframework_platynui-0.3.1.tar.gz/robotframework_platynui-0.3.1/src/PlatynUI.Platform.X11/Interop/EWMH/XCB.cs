using System.Runtime.InteropServices;
using static PlatynUI.Platform.X11.Interop.XCB.xcb_atom_enum_t;

namespace PlatynUI.Platform.X11.Interop.XCB;

public static unsafe partial class XCB
{
    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_intern_atom_cookie_t* xcb_ewmh_init_atoms(xcb_connection_t* c, xcb_ewmh_connection_t* ewmh);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_init_atoms_replies(xcb_ewmh_connection_t* ewmh, xcb_intern_atom_cookie_t* ewmh_cookies, xcb_generic_error_t** e);

    public static void xcb_ewmh_connection_wipe(xcb_ewmh_connection_t* ewmh)
    {
        free(ewmh->screens);
        free(ewmh->_NET_WM_CM_Sn);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_send_client_message(xcb_connection_t* c, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_window_t")] uint dest, [NativeTypeName("xcb_atom_t")] uint atom, [NativeTypeName("uint32_t")] uint data_len, [NativeTypeName("const uint32_t *")] uint* data);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_window_from_reply([NativeTypeName("xcb_window_t *")] uint* window, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_window_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("xcb_window_t *")] uint* window, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_cardinal_from_reply([NativeTypeName("uint32_t *")] uint* cardinal, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_cardinal_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* cardinal, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_atoms_from_reply(xcb_ewmh_get_atoms_reply_t* atoms, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_atoms_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_atoms_reply_t* atoms, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_atoms_reply_wipe(xcb_ewmh_get_atoms_reply_t* data);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_windows_from_reply(xcb_ewmh_get_windows_reply_t* atoms, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_utf8_strings_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_utf8_strings_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_windows_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_windows_reply_t* atoms, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_windows_reply_wipe(xcb_ewmh_get_windows_reply_t* data);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_utf8_strings_reply_wipe(xcb_ewmh_get_utf8_strings_reply_t* data);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_supported(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_supported_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_supported_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_supported(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_supported_from_reply(xcb_ewmh_get_atoms_reply_t* supported, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_atoms_from_reply(supported, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_supported_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_atoms_reply_t* supported, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_atoms_reply(ewmh, cookie, supported, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_client_list(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_client_list_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_client_list_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_client_list(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_client_list_from_reply(xcb_ewmh_get_windows_reply_t* clients, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_windows_from_reply(clients, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_client_list_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_windows_reply_t* clients, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_windows_reply(ewmh, cookie, clients, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_client_list_stacking(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_client_list_stacking_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_client_list_stacking_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_client_list_stacking(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_client_list_stacking_from_reply(xcb_ewmh_get_windows_reply_t* clients, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_windows_from_reply(clients, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_client_list_stacking_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_windows_reply_t* clients, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_windows_reply(ewmh, cookie, clients, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_number_of_desktops(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint number_of_desktops);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_number_of_desktops_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint number_of_desktops);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_number_of_desktops_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_number_of_desktops(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_number_of_desktops_from_reply([NativeTypeName("uint32_t *")] uint* number_of_desktops, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(number_of_desktops, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_number_of_desktops_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* number_of_desktops, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, number_of_desktops, e);
    }

    public static xcb_void_cookie_t xcb_ewmh_request_change_number_of_desktops(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_number_of_desktops)
    {
        return xcb_ewmh_send_client_message(ewmh->connection, 0, ewmh->screens[screen_nbr]->root, ewmh->_NET_NUMBER_OF_DESKTOPS, (uint)(sizeof(uint)), &new_number_of_desktops);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_geometry(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_width, [NativeTypeName("uint32_t")] uint new_height);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_geometry_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_width, [NativeTypeName("uint32_t")] uint new_height);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_geometry_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_geometry(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_desktop_geometry(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_width, [NativeTypeName("uint32_t")] uint new_height);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_geometry_from_reply([NativeTypeName("uint32_t *")] uint* width, [NativeTypeName("uint32_t *")] uint* height, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_geometry_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* width, [NativeTypeName("uint32_t *")] uint* height, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_viewport(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, xcb_ewmh_coordinates_t* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_viewport_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, xcb_ewmh_coordinates_t* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_viewport_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_viewport(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_desktop_viewport(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint x, [NativeTypeName("uint32_t")] uint y);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_viewport_from_reply(xcb_ewmh_get_desktop_viewport_reply_t* vp, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_viewport_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_desktop_viewport_reply_t* vp, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_desktop_viewport_reply_wipe(xcb_ewmh_get_desktop_viewport_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_current_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_current_desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_current_desktop_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_current_desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_current_desktop_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_current_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_current_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint new_desktop, [NativeTypeName("xcb_timestamp_t")] uint timestamp);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_current_desktop_from_reply([NativeTypeName("uint32_t *")] uint* current_desktop, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(current_desktop, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_current_desktop_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* current_desktop, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, current_desktop, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_names(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_names_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_names_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_names(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_desktop_names_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* names, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_utf8_strings_from_reply(ewmh, names, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_desktop_names_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* names, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_utf8_strings_reply(ewmh, cookie, names, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_active_window(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint new_active_window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_active_window_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint new_active_window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_active_window(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint window_to_activate, xcb_ewmh_client_source_type_t source_indication, [NativeTypeName("xcb_timestamp_t")] uint timestamp, [NativeTypeName("xcb_window_t")] uint current_active_window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_active_window_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_active_window(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_active_window_from_reply([NativeTypeName("xcb_window_t *")] uint* active_window, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_window_from_reply(active_window, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_active_window_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("xcb_window_t *")] uint* active_window, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_window_reply(ewmh, cookie, active_window, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_workarea(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, xcb_ewmh_geometry_t* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_workarea_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, xcb_ewmh_geometry_t* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_workarea_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_workarea(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_workarea_from_reply(xcb_ewmh_get_workarea_reply_t* wa, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_workarea_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_workarea_reply_t* wa, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_workarea_reply_wipe(xcb_ewmh_get_workarea_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_supporting_wm_check(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint parent_window, [NativeTypeName("xcb_window_t")] uint child_window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_supporting_wm_check_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint parent_window, [NativeTypeName("xcb_window_t")] uint child_window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_supporting_wm_check_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_supporting_wm_check(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_supporting_wm_check_from_reply([NativeTypeName("xcb_window_t *")] uint* window, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_window_from_reply(window, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_supporting_wm_check_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("xcb_window_t *")] uint* window, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_window_reply(ewmh, cookie, window, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_virtual_roots(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_virtual_roots_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_window_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_virtual_roots_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_virtual_roots(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_virtual_roots_from_reply(xcb_ewmh_get_windows_reply_t* virtual_roots, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_windows_from_reply(virtual_roots, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_virtual_roots_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_windows_reply_t* virtual_roots, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_windows_reply(ewmh, cookie, virtual_roots, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_layout(xcb_ewmh_connection_t* ewmh, int screen_nbr, xcb_ewmh_desktop_layout_orientation_t orientation, [NativeTypeName("uint32_t")] uint columns, [NativeTypeName("uint32_t")] uint rows, xcb_ewmh_desktop_layout_starting_corner_t starting_corner);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_desktop_layout_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, xcb_ewmh_desktop_layout_orientation_t orientation, [NativeTypeName("uint32_t")] uint columns, [NativeTypeName("uint32_t")] uint rows, xcb_ewmh_desktop_layout_starting_corner_t starting_corner);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_layout_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_desktop_layout(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_layout_from_reply(xcb_ewmh_get_desktop_layout_reply_t* desktop_layouts, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_desktop_layout_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_desktop_layout_reply_t* desktop_layouts, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_showing_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_showing_desktop_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_showing_desktop_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_showing_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_showing_desktop_from_reply([NativeTypeName("uint32_t *")] uint* desktop, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(desktop, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_showing_desktop_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* desktop, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, desktop, e);
    }

    public static xcb_void_cookie_t xcb_ewmh_request_change_showing_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("uint32_t")] uint enter)
    {
        return xcb_ewmh_send_client_message(ewmh->connection, 0, ewmh->screens[screen_nbr]->root, ewmh->_NET_SHOWING_DESKTOP, (uint)(sizeof(uint)), &enter);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_close_window(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint window_to_close, [NativeTypeName("xcb_timestamp_t")] uint timestamp, xcb_ewmh_client_source_type_t source_indication);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_moveresize_window(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint moveresize_window, xcb_gravity_t gravity, xcb_ewmh_client_source_type_t source_indication, xcb_ewmh_moveresize_window_opt_flags_t flags, [NativeTypeName("uint32_t")] uint x, [NativeTypeName("uint32_t")] uint y, [NativeTypeName("uint32_t")] uint width, [NativeTypeName("uint32_t")] uint height);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_wm_moveresize(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint moveresize_window, [NativeTypeName("uint32_t")] uint x_root, [NativeTypeName("uint32_t")] uint y_root, xcb_ewmh_moveresize_direction_t direction, xcb_button_index_t button, xcb_ewmh_client_source_type_t source_indication);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_restack_window(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint window_to_restack, [NativeTypeName("xcb_window_t")] uint sibling_window, xcb_stack_mode_t detail);

    public static xcb_void_cookie_t xcb_ewmh_request_frame_extents(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint client_window)
    {
        return xcb_ewmh_send_client_message(ewmh->connection, client_window, ewmh->screens[screen_nbr]->root, ewmh->_NET_REQUEST_FRAME_EXTENTS, 0, null);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_name_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_name_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_name_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_utf8_strings_from_reply(ewmh, data, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_name_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_utf8_strings_reply(ewmh, cookie, data, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_visible_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_visible_name_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_visible_name_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_visible_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_visible_name_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_utf8_strings_from_reply(ewmh, data, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_visible_name_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_utf8_strings_reply(ewmh, cookie, data, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_icon_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_icon_name_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon_name_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_icon_name_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_utf8_strings_from_reply(ewmh, data, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_icon_name_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_utf8_strings_reply(ewmh, cookie, data, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_visible_icon_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_visible_icon_name_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint strings_len, [NativeTypeName("const char *")] sbyte* strings);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_visible_icon_name_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_visible_icon_name(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_visible_icon_name_from_reply(xcb_ewmh_connection_t* ewmh, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_utf8_strings_from_reply(ewmh, data, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_visible_icon_name_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_utf8_strings_reply_t* data, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_utf8_strings_reply(ewmh, cookie, data, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_desktop(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_desktop_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint desktop);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_desktop_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_desktop(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_desktop_from_reply([NativeTypeName("uint32_t *")] uint* desktop, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(desktop, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_desktop_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* desktop, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, desktop, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_wm_desktop(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint client_window, [NativeTypeName("uint32_t")] uint new_desktop, xcb_ewmh_client_source_type_t source_indication);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_window_type(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_window_type_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_window_type_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_window_type(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_window_type_from_reply(xcb_ewmh_get_atoms_reply_t* wtypes, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_window_type_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_atoms_reply_t* name, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_state(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_state_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_state_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_state(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_state_from_reply(xcb_ewmh_get_atoms_reply_t* wtypes, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_state_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_atoms_reply_t* name, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_wm_state(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint client_window, xcb_ewmh_wm_state_action_t action, [NativeTypeName("xcb_atom_t")] uint first_property, [NativeTypeName("xcb_atom_t")] uint second_property, xcb_ewmh_client_source_type_t source_indication);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_allowed_actions(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_allowed_actions_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint list_len, [NativeTypeName("xcb_atom_t *")] uint* list);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_allowed_actions_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_allowed_actions(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_allowed_actions_from_reply(xcb_ewmh_get_atoms_reply_t* wtypes, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_allowed_actions_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_atoms_reply_t* name, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_strut(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_strut_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_strut_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_strut(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_strut_from_reply(xcb_ewmh_get_extents_reply_t* struts, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_strut_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_extents_reply_t* struts, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_strut_partial(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, xcb_ewmh_wm_strut_partial_t wm_strut);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_strut_partial_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, xcb_ewmh_wm_strut_partial_t wm_strut);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_strut_partial_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_strut_partial(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_strut_partial_from_reply(xcb_ewmh_wm_strut_partial_t* struts, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_strut_partial_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_wm_strut_partial_t* struts, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_icon_geometry(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_icon_geometry_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon_geometry_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon_geometry(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_icon_geometry_from_reply(xcb_ewmh_geometry_t* icons, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_icon_geometry_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_geometry_t* icons, xcb_generic_error_t** e);

    public static xcb_void_cookie_t xcb_ewmh_set_wm_icon_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("uint8_t")] byte mode, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint data_len, [NativeTypeName("uint32_t *")] uint* data)
    {
        return xcb_change_property_checked(ewmh->connection, mode, window, ewmh->_NET_WM_ICON, (uint)(XCB_ATOM_CARDINAL), 32, data_len, data);
    }

    public static xcb_void_cookie_t xcb_ewmh_set_wm_icon(xcb_ewmh_connection_t* ewmh, [NativeTypeName("uint8_t")] byte mode, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint data_len, [NativeTypeName("uint32_t *")] uint* data)
    {
        return xcb_change_property(ewmh->connection, mode, window, ewmh->_NET_WM_ICON, (uint)(XCB_ATOM_CARDINAL), 32, data_len, data);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_append_wm_icon_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint width, [NativeTypeName("uint32_t")] uint height, [NativeTypeName("uint32_t")] uint img_len, [NativeTypeName("uint32_t *")] uint* img);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_append_wm_icon(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint width, [NativeTypeName("uint32_t")] uint height, [NativeTypeName("uint32_t")] uint img_len, [NativeTypeName("uint32_t *")] uint* img);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_icon(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_icon_from_reply(xcb_ewmh_get_wm_icon_reply_t* wm_icon, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_icon_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_wm_icon_reply_t* wm_icon, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_ewmh_wm_icon_iterator_t xcb_ewmh_get_wm_icon_iterator([NativeTypeName("const xcb_ewmh_get_wm_icon_reply_t *")] xcb_ewmh_get_wm_icon_reply_t* wm_icon);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("unsigned int")]
    public static extern uint xcb_ewmh_get_wm_icon_length([NativeTypeName("const xcb_ewmh_get_wm_icon_reply_t *")] xcb_ewmh_get_wm_icon_reply_t* wm_icon);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_wm_icon_next(xcb_ewmh_wm_icon_iterator_t* iterator);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern void xcb_ewmh_get_wm_icon_reply_wipe(xcb_ewmh_get_wm_icon_reply_t* wm_icon);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_pid(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint pid);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_pid_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint pid);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_pid_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_pid(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_pid_from_reply([NativeTypeName("uint32_t *")] uint* pid, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(pid, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_pid_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* pid, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, pid, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_handled_icons(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint handled_icons);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_handled_icons_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint handled_icons);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_handled_icons_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_handled_icons(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_handled_icons_from_reply([NativeTypeName("uint32_t *")] uint* handled_icons, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(handled_icons, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_handled_icons_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* handled_icons, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, handled_icons, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_user_time(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint xtime);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_user_time_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint pid);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_user_time_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_user_time(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_user_time_from_reply([NativeTypeName("uint32_t *")] uint* xtime, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(xtime, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_user_time_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* xtime, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, xtime, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_user_time_window(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint xtime);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_user_time_window_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint pid);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_user_time_window_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_user_time_window(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_user_time_window_from_reply([NativeTypeName("uint32_t *")] uint* xtime, xcb_get_property_reply_t* r)
    {
        return xcb_ewmh_get_cardinal_from_reply(xtime, r);
    }

    [return: NativeTypeName("uint8_t")]
    public static byte xcb_ewmh_get_wm_user_time_window_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint32_t *")] uint* xtime, xcb_generic_error_t** e)
    {
        return xcb_ewmh_get_cardinal_reply(ewmh, cookie, xtime, e);
    }

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_frame_extents(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_frame_extents_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_frame_extents_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_frame_extents(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_frame_extents_from_reply(xcb_ewmh_get_extents_reply_t* frame_extents, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_frame_extents_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_extents_reply_t* frame_extents, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_send_wm_ping(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_timestamp_t")] uint timestamp);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_sync_request_counter(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_sync_request_counter_atom, [NativeTypeName("uint32_t")] uint low, [NativeTypeName("uint32_t")] uint high);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_sync_request_counter_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_sync_request_counter_atom, [NativeTypeName("uint32_t")] uint low, [NativeTypeName("uint32_t")] uint high);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_sync_request_counter_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_sync_request_counter(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_sync_request_counter_from_reply([NativeTypeName("uint64_t *")] nuint* counter, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_sync_request_counter_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, [NativeTypeName("uint64_t *")] nuint* counter, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_send_wm_sync_request(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("xcb_atom_t")] uint wm_protocols_atom, [NativeTypeName("xcb_atom_t")] uint wm_sync_request_atom, [NativeTypeName("xcb_timestamp_t")] uint timestamp, [NativeTypeName("uint64_t")] nuint counter);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_fullscreen_monitors(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_fullscreen_monitors_checked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_fullscreen_monitors_unchecked(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_property_cookie_t xcb_ewmh_get_wm_fullscreen_monitors(xcb_ewmh_connection_t* ewmh, [NativeTypeName("xcb_window_t")] uint window);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_fullscreen_monitors_from_reply(xcb_ewmh_get_wm_fullscreen_monitors_reply_t* monitors, xcb_get_property_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_fullscreen_monitors_reply(xcb_ewmh_connection_t* ewmh, xcb_get_property_cookie_t cookie, xcb_ewmh_get_wm_fullscreen_monitors_reply_t* monitors, xcb_generic_error_t** e);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_request_change_wm_fullscreen_monitors(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint window, [NativeTypeName("uint32_t")] uint top, [NativeTypeName("uint32_t")] uint bottom, [NativeTypeName("uint32_t")] uint left, [NativeTypeName("uint32_t")] uint right, xcb_ewmh_client_source_type_t source_indication);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_cm_owner(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint owner, [NativeTypeName("xcb_timestamp_t")] uint timestamp, [NativeTypeName("uint32_t")] uint selection_data1, [NativeTypeName("uint32_t")] uint selection_data2);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_void_cookie_t xcb_ewmh_set_wm_cm_owner_checked(xcb_ewmh_connection_t* ewmh, int screen_nbr, [NativeTypeName("xcb_window_t")] uint owner, [NativeTypeName("xcb_timestamp_t")] uint timestamp, [NativeTypeName("uint32_t")] uint selection_data1, [NativeTypeName("uint32_t")] uint selection_data2);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_selection_owner_cookie_t xcb_ewmh_get_wm_cm_owner_unchecked(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    public static extern xcb_get_selection_owner_cookie_t xcb_ewmh_get_wm_cm_owner(xcb_ewmh_connection_t* ewmh, int screen_nbr);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_cm_owner_from_reply([NativeTypeName("xcb_window_t *")] uint* owner, xcb_get_selection_owner_reply_t* r);

    [DllImport("xcb-ewmh", CallingConvention = CallingConvention.Cdecl, ExactSpelling = true)]
    [return: NativeTypeName("uint8_t")]
    public static extern byte xcb_ewmh_get_wm_cm_owner_reply(xcb_ewmh_connection_t* ewmh, xcb_get_selection_owner_cookie_t cookie, [NativeTypeName("xcb_window_t *")] uint* owner, xcb_generic_error_t** e);
}
