using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_colormap_notify_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("xcb_window_t")]
    public uint window;

    [NativeTypeName("xcb_colormap_t")]
    public uint colormap;

    [NativeTypeName("uint8_t")]
    public byte _new;

    [NativeTypeName("uint8_t")]
    public byte state;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
