using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_circulate_notify_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("xcb_window_t")]
    public uint @event;

    [NativeTypeName("xcb_window_t")]
    public uint window;

    [NativeTypeName("uint8_t[4]")]
    public _pad1_e__FixedBuffer pad1;

    [NativeTypeName("uint8_t")]
    public byte place;

    [NativeTypeName("uint8_t[3]")]
    public _pad2_e__FixedBuffer pad2;

    [InlineArray(4)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(3)]
    public partial struct _pad2_e__FixedBuffer
    {
        public byte e0;
    }
}
