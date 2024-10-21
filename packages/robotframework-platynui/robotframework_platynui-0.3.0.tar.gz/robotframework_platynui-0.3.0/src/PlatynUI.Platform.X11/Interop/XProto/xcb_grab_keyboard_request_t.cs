using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_grab_keyboard_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte owner_events;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_window_t")]
    public uint grab_window;

    [NativeTypeName("xcb_timestamp_t")]
    public uint time;

    [NativeTypeName("uint8_t")]
    public byte pointer_mode;

    [NativeTypeName("uint8_t")]
    public byte keyboard_mode;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
