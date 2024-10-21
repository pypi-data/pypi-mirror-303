namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_ewmh_connection_t
{
    public xcb_connection_t* connection;

    public xcb_screen_t** screens;

    public int nb_screens;

    [NativeTypeName("xcb_atom_t *")]
    public uint* _NET_WM_CM_Sn;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_SUPPORTED;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_CLIENT_LIST;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_CLIENT_LIST_STACKING;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_NUMBER_OF_DESKTOPS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_DESKTOP_GEOMETRY;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_DESKTOP_VIEWPORT;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_CURRENT_DESKTOP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_DESKTOP_NAMES;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_ACTIVE_WINDOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WORKAREA;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_SUPPORTING_WM_CHECK;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_VIRTUAL_ROOTS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_DESKTOP_LAYOUT;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_SHOWING_DESKTOP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_CLOSE_WINDOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_MOVERESIZE_WINDOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_MOVERESIZE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_RESTACK_WINDOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_REQUEST_FRAME_EXTENTS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_NAME;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_VISIBLE_NAME;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ICON_NAME;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_VISIBLE_ICON_NAME;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_DESKTOP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ALLOWED_ACTIONS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STRUT;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STRUT_PARTIAL;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ICON_GEOMETRY;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ICON;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_PID;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_HANDLED_ICONS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_USER_TIME;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_USER_TIME_WINDOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_FRAME_EXTENTS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_PING;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_SYNC_REQUEST;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_SYNC_REQUEST_COUNTER;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_FULLSCREEN_MONITORS;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_FULL_PLACEMENT;

    [NativeTypeName("xcb_atom_t")]
    public uint UTF8_STRING;

    [NativeTypeName("xcb_atom_t")]
    public uint WM_PROTOCOLS;

    [NativeTypeName("xcb_atom_t")]
    public uint MANAGER;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_DESKTOP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_DOCK;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_TOOLBAR;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_MENU;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_UTILITY;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_SPLASH;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_DIALOG;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_DROPDOWN_MENU;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_POPUP_MENU;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_TOOLTIP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_NOTIFICATION;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_COMBO;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_DND;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_WINDOW_TYPE_NORMAL;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_MODAL;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_STICKY;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_MAXIMIZED_VERT;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_MAXIMIZED_HORZ;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_SHADED;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_SKIP_TASKBAR;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_SKIP_PAGER;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_HIDDEN;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_FULLSCREEN;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_ABOVE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_BELOW;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_STATE_DEMANDS_ATTENTION;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_MOVE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_RESIZE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_MINIMIZE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_SHADE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_STICK;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_MAXIMIZE_HORZ;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_MAXIMIZE_VERT;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_FULLSCREEN;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_CHANGE_DESKTOP;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_CLOSE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_ABOVE;

    [NativeTypeName("xcb_atom_t")]
    public uint _NET_WM_ACTION_BELOW;
}
