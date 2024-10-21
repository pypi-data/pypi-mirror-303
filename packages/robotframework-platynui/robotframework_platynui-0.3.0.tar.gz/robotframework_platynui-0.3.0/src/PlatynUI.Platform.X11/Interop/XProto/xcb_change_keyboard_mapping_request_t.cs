using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_change_keyboard_mapping_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte keycode_count;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_keycode_t")]
    public byte first_keycode;

    [NativeTypeName("uint8_t")]
    public byte keysyms_per_keycode;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
