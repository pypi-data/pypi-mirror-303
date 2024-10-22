namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_charinfo_iterator_t
{
    public xcb_charinfo_t* data;

    public int rem;

    public int index;
}
