namespace PlatynUI.Platform.X11.Interop.XCB;

public unsafe partial struct xcb_coloritem_iterator_t
{
    public xcb_coloritem_t* data;

    public int rem;

    public int index;
}
