// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0


using PlatynUI.Platform.X11.Interop.XCB;
using PlatynUI.Runtime;
using static PlatynUI.Platform.X11.Interop.XCB.XCB;

namespace PlatynUI.Platform.X11;

[Serializable]
public class X11Exception : Exception
{
    public X11Exception() { }

    public X11Exception(string? message)
        : base(message) { }

    public X11Exception(string? message, Exception? innerException)
        : base(message, innerException) { }
}

public unsafe class XCBConnection : IDisposable
{
    private static XCBConnection? _instance = null;
    private xcb_connection_t* _connection = null;

    public XCBConnection()
    {
        Connect();
        Atoms = new BuiltinAtoms(this);
    }

    ~XCBConnection()
    {
        Disconnect();
    }

    public static XCBConnection Default => _instance ??= new XCBConnection();

    private void Disconnect()
    {
        if (_connection != null)
        {
            xcb_disconnect(_connection);
        }
        _connection = null;
    }

    public static implicit operator xcb_connection_t*(XCBConnection c) => c.Connection;

    public xcb_connection_t* Connection
    {
        get
        {
            if (_connection == null)
            {
                throw new X11Exception("Not Connected");
            }
            return _connection;
        }
    }

    private xcb_connection_t* Connect()
    {
        if (_connection != null)
        {
            throw new X11Exception("Allready connected.");
        }

        _connection = xcb_connect(null, null);

        if (_connection == null)
        {
            throw new X11Exception("Can't connect to Display");
        }
        return _connection;
    }

    public void Dispose()
    {
        // Dispose of unmanaged resources.
        Dispose(true);
        // Suppress finalization.
        GC.SuppressFinalize(this);
    }

    private bool _disposed = false;

    protected virtual void Dispose(bool disposing)
    {
        if (_disposed)
        {
            return;
        }

        if (disposing)
        {
            Disconnect();
        }

        _disposed = true;
    }

    public uint RootWindow
    {
        get { return Screen->root; }
    }

    public uint RootVisual => Screen->root_visual;

    public Size ScreenSize
    {
        get { return new Size(Screen->width_in_pixels, Screen->height_in_pixels); }
    }

    private xcb_screen_t* _screen = null;
    public xcb_screen_t* Screen
    {
        get
        {
            if (_screen == null)
            {
                _screen = xcb_setup_roots_iterator(xcb_get_setup(Connection)).data;
            }
            return _screen;
        }
    }

    bool hasEwmh = false;

    xcb_ewmh_connection_t _ewmhConnection;
    public xcb_ewmh_connection_t Ewmh
    {
        get
        {
            if (!hasEwmh)
            {
                hasEwmh = true;

                xcb_ewmh_connection_t ewmh_connection;

                var ewmh_cookie = xcb_ewmh_init_atoms(this, &ewmh_connection);
                xcb_ewmh_init_atoms_replies(&ewmh_connection, ewmh_cookie, null);

                _ewmhConnection = ewmh_connection;
            }
            return _ewmhConnection;
        }
    }

    public bool HasEwmh => Ewmh.connection != null;

    unsafe uint CreateInternAtom(string name)
    {
        fixed (sbyte* chars = Array.ConvertAll(System.Text.Encoding.UTF8.GetBytes(name), Convert.ToSByte))
        {
            var utf8_string_cookie = xcb_intern_atom(this._connection, 0, (ushort)name.Length, chars);

            var reply = xcb_intern_atom_reply(this, utf8_string_cookie, null);
            return reply->atom;
        }
    }

    public class BuiltinAtoms(XCBConnection connection)
    {
        public uint _NET_WM_BYPASS_COMPOSITOR = connection.CreateInternAtom("_NET_WM_BYPASS_COMPOSITOR");
        public uint _KDE_NET_WM_WINDOW_TYPE_OVERRIDE = connection.CreateInternAtom("_KDE_NET_WM_WINDOW_TYPE_OVERRIDE");
        public uint WM_CLIENT_LEADER = connection.CreateInternAtom("WM_CLIENT_LEADER");

        public uint _MOTIF_WM_HINTS = connection.CreateInternAtom("_MOTIF_WM_HINTS");
    }

    public BuiltinAtoms Atoms { get; }
}
