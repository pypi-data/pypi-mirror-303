// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0


using System.Diagnostics;
using PlatynUI.Platform.X11.Interop.XCB;
using PlatynUI.Runtime;
using static PlatynUI.Platform.X11.Interop.XCB.XCB;

namespace PlatynUI.Platform.X11;

internal class Line : IDisposable
{
    private bool _disposed;

    public uint Id { get; private set; }
    public XCBConnection Connection { get; }
    public bool Valid { get; private set; }

    private Rect _position;

    string Title { get; set; }

    public Line(XCBConnection connection, string title)
    {
        Connection = connection;

        Title = title;

        Valid = false;

        unsafe
        {
            Id = xcb_generate_id(Connection);

            fixed (
                void* data = new uint[]
                {
                    0xff0000, // RED
                    1,
                    0,
                    (uint)xcb_event_mask_t.XCB_EVENT_MASK_EXPOSURE,
                }
            )
            {
                var cookie = xcb_create_window_checked(
                    Connection,
                    (byte)XCB_COPY_FROM_PARENT,
                    Id,
                    Connection.RootWindow,
                    1,
                    1,
                    1,
                    1,
                    0,
                    (ushort)xcb_window_class_t.XCB_WINDOW_CLASS_INPUT_OUTPUT,
                    Connection.RootVisual,
                    (uint)xcb_cw_t.XCB_CW_BACK_PIXEL
                        | (uint)xcb_cw_t.XCB_CW_OVERRIDE_REDIRECT
                        | (uint)xcb_cw_t.XCB_CW_SAVE_UNDER
                        | (uint)xcb_cw_t.XCB_CW_EVENT_MASK,
                    data
                );

                var error = xcb_request_check(Connection.Connection, cookie);
                if (error != null)
                {
                    Debug.WriteLine($"Error: Can't create XCB Window {error->error_code}");
                    free(error);
                    return;
                }
            }

            var title_ascii = System.Text.Encoding.ASCII.GetBytes(Title);
            fixed (void* data = title_ascii)
                xcb_change_property(
                    Connection,
                    (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                    Id,
                    (uint)xcb_atom_enum_t.XCB_ATOM_WM_NAME,
                    (uint)xcb_atom_enum_t.XCB_ATOM_STRING,
                    8,
                    (uint)title_ascii.Length,
                    data
                );

            if (Connection.HasEwmh)
            {
                var title_utf8 = System.Text.Encoding.UTF8.GetBytes(title);
                fixed (void* data = title_utf8)
                    xcb_change_property(
                        Connection,
                        (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                        Id,
                        (uint)xcb_atom_enum_t.XCB_ATOM_WM_NAME,
                        Connection.Ewmh.UTF8_STRING,
                        8,
                        (uint)title_utf8.Length,
                        data
                    );

                fixed (
                    void* data = new uint[]
                    {
                        Connection.Ewmh._NET_WM_WINDOW_TYPE_TOOLTIP,
                        Connection.Atoms._KDE_NET_WM_WINDOW_TYPE_OVERRIDE,
                        Connection.Ewmh._NET_WM_WINDOW_TYPE_NORMAL
                    }
                )
                    xcb_change_property(
                        XCBConnection.Default.Connection,
                        (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                        Id,
                        Connection.Ewmh._NET_WM_WINDOW_TYPE,
                        (uint)xcb_atom_enum_t.XCB_ATOM_ATOM,
                        32,
                        3,
                        data
                    );

                fixed (
                    void* data = new uint[]
                    {
                        Connection.Ewmh._NET_WM_STATE_ABOVE,
                        Connection.Ewmh._NET_WM_STATE_SKIP_TASKBAR,
                        Connection.Ewmh._NET_WM_STATE_SKIP_PAGER,
                    }
                )
                    xcb_change_property(
                        XCBConnection.Default.Connection,
                        (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                        Id,
                        Connection.Ewmh._NET_WM_STATE,
                        (uint)xcb_atom_enum_t.XCB_ATOM_ATOM,
                        32,
                        3,
                        data
                    );
            }

            MotifHints motifHints =
                new()
                {
                    Flags = MotifHints.MWM_HINTS_DECORATIONS,
                    Decorations = 0,
                    Functions = 0
                };

            if (Connection.Atoms._MOTIF_WM_HINTS != 0)
            {
                xcb_change_property(
                    XCBConnection.Default.Connection,
                    (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                    Id,
                    Connection.Atoms._MOTIF_WM_HINTS,
                    Connection.Atoms._MOTIF_WM_HINTS,
                    32,
                    5,
                    &motifHints
                );
            }

            if (Connection.Atoms._NET_WM_BYPASS_COMPOSITOR != 0)
            {
                fixed (void* data = new uint[] { 2 })
                {
                    xcb_change_property(
                        XCBConnection.Default.Connection,
                        (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                        Id,
                        Connection.Atoms._NET_WM_BYPASS_COMPOSITOR,
                        (uint)xcb_atom_enum_t.XCB_ATOM_CARDINAL,
                        32,
                        1,
                        data
                    );
                }
            }

            fixed (void* data = new uint[] { Connection.RootWindow })
            {
                xcb_change_property(
                    XCBConnection.Default.Connection,
                    (byte)xcb_prop_mode_t.XCB_PROP_MODE_REPLACE,
                    Id,
                    (uint)xcb_atom_enum_t.XCB_ATOM_WM_TRANSIENT_FOR,
                    (uint)xcb_atom_enum_t.XCB_ATOM_WINDOW,
                    32,
                    1,
                    data
                );
            }

            _ = xcb_flush(Connection);
        }
        Valid = true;
    }

    public Rect Position
    {
        get => _position;
        set
        {
            _position = value;

            if (!Valid)
                return;

            unsafe
            {
                fixed (
                    void* data = new uint[]
                    {
                        (uint)_position.X,
                        (uint)_position.Y,
                        (uint)_position.Width,
                        (uint)_position.Height
                    }
                )
                {
                    xcb_configure_window(
                        XCBConnection.Default.Connection,
                        Id,
                        (ushort)xcb_config_window_t.XCB_CONFIG_WINDOW_X
                            | (ushort)xcb_config_window_t.XCB_CONFIG_WINDOW_Y
                            | (ushort)xcb_config_window_t.XCB_CONFIG_WINDOW_WIDTH
                            | (ushort)xcb_config_window_t.XCB_CONFIG_WINDOW_HEIGHT,
                        data
                    );
                    _ = xcb_flush(Connection);
                }
            }
        }
    }

    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    private void Dispose(bool disposing)
    {
        if (_disposed)
        {
            return;
        }

        if (disposing)
        {
            // NONE
        }

        _disposed = true;

        if (Valid)
        {
            unsafe
            {
                xcb_destroy_window(Connection, Id);
                _ = xcb_flush(Connection);
            }
        }
        Id = 0;
        Valid = false;
    }

    ~Line()
    {
        Dispose(false);
    }

    internal void Hide()
    {
        if (Valid)
        {
            unsafe
            {
                xcb_unmap_window(Connection, Id);
                _ = xcb_flush(Connection);
            }
        }
    }

    internal void Close()
    {
        Hide();
    }

    internal void Show()
    {
        if (Valid)
        {
            unsafe
            {
                xcb_map_window(Connection, Id);
                _ = xcb_flush(Connection);
            }
        }
    }
}
