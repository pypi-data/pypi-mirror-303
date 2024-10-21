using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_get_keyboard_control_reply_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t")]
    public byte global_auto_repeat;

    [NativeTypeName("uint16_t")]
    public ushort sequence;

    [NativeTypeName("uint32_t")]
    public uint length;

    [NativeTypeName("uint32_t")]
    public uint led_mask;

    [NativeTypeName("uint8_t")]
    public byte key_click_percent;

    [NativeTypeName("uint8_t")]
    public byte bell_percent;

    [NativeTypeName("uint16_t")]
    public ushort bell_pitch;

    [NativeTypeName("uint16_t")]
    public ushort bell_duration;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [NativeTypeName("uint8_t[32]")]
    public _auto_repeats_e__FixedBuffer auto_repeats;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }

    [InlineArray(32)]
    public partial struct _auto_repeats_e__FixedBuffer
    {
        public byte e0;
    }
}
