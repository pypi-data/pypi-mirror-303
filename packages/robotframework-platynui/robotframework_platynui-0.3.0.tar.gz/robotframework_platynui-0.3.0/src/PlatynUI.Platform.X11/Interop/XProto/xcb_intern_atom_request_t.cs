using System.Runtime.CompilerServices;

namespace PlatynUI.Platform.X11.Interop.XCB;

public partial struct xcb_intern_atom_request_t
{
    [NativeTypeName("uint8_t")]
    public byte major_opcode;

    [NativeTypeName("uint8_t")]
    public byte only_if_exists;

    [NativeTypeName("uint16_t")]
    public ushort length;

    [NativeTypeName("uint16_t")]
    public ushort name_len;

    [NativeTypeName("uint8_t[2]")]
    public _pad0_e__FixedBuffer pad0;

    [InlineArray(2)]
    public partial struct _pad0_e__FixedBuffer
    {
        public byte e0;
    }
}
