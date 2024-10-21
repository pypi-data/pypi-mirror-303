using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_change_property_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte mode;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("xcb_window_t")]
    public uint window;

    [NativeTypeName("xcb_atom_t")]
    public uint property;

    [NativeTypeName("xcb_atom_t")]
    public uint type;

    [NativeTypeName("uint8_t")]
    public byte format;

    [NativeTypeName("uint8_t[3]")]
    public _pad0_e__FixedBuffer pad0;

    [NativeTypeName("uint32_t")]
    public uint data_len;

    [InlineArray(3)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
