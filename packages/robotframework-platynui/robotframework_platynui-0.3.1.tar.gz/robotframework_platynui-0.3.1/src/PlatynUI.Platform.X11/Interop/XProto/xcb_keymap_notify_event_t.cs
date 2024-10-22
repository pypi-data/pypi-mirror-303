using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_keymap_notify_event_t
{
    [NativeTypeName("uint8_t")]
    public byte response_type;

    [NativeTypeName("uint8_t[31]")]
    public _keys_e__FixedBuffer keys;

    [InlineArray(31)]
    public partial struct _keys_e__FixedBuffer
    {
        public byte e0;
    }
}
