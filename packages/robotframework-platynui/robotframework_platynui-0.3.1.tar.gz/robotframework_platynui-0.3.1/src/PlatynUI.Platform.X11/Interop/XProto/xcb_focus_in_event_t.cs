using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_focus_in_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte detail;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("xcb_window_t")]
    public uint @event;

    [NativeTypeName("uint8_t")]
    public byte mode;

    [NativeTypeName("uint8_t[3]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(3)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
