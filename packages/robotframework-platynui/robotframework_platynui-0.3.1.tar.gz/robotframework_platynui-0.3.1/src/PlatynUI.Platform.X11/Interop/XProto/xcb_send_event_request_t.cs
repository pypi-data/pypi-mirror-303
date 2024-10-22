using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_send_event_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte propagate;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_window_t")]
    public uint destination;

    [NativeTypeName("uint32_t")]
    public uint event_mask;

    [NativeTypeName("char[32]")]
    public _event_e__FixedBuffer @event;

    [InlineArray(32)]
    public partial struct _event_e__FixedBuffer
    {
        public sbyte e0;
    }
}
