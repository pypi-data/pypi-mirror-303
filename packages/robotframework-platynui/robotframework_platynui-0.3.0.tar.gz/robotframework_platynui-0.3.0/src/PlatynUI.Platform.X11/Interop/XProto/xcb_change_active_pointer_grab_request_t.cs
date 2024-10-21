using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_change_active_pointer_grab_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte pad0;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_cursor_t")]
    public uint cursor;

    [NativeTypeName("xcb_timestamp_t")]
    public uint time;

    [NativeTypeName("uint16_t")]
    public ushort event_mask;

    [NativeTypeName("uint8_t[2]")]
    public _pad1_e__FixedBuffer pad1;

    [InlineArray(2)]
    public partial struct _pad1_e__FixedBuffer
    {
        public byte e0;
    }
}
