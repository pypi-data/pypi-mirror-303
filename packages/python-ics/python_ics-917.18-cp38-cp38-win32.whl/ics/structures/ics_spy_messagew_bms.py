# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless39357(ctypes.Structure):
    _fields_ = [
        ('', ctypes.c_uint32, 8),
        ('PacketType', ctypes.c_uint32, 8),
        ('PacketID', ctypes.c_uint32, 8),
        ('PacketSource', ctypes.c_uint32, 8),
    ]



class Nameless20257(ctypes.Union):
    _anonymous_  = ('Nameless39357',)
    _fields_ = [
        ('ArbIDOrHeader', ctypes.c_uint32),
        ('Nameless39357', Nameless39357),
    ]



class Nameless60883(ctypes.Structure):
    _fields_ = [
        ('APICode', ctypes.c_uint32, 8),
        ('', ctypes.c_uint32, 24),
    ]



class Nameless5382(ctypes.Union):
    _anonymous_  = ('Nameless60883',)
    _fields_ = [
        ('StatusBitField3', ctypes.c_uint32),
        ('Nameless60883', Nameless60883),
    ]



class Nameless50617(ctypes.Structure):
    _anonymous_  = ('Nameless5382',)
    _fields_ = [
        ('Nameless5382', Nameless5382),
        ('StatusBitField4', ctypes.c_uint32),
    ]



class Nameless45821(ctypes.Union):
    _anonymous_  = ('Nameless50617',)
    _fields_ = [
        ('Nameless50617', Nameless50617),
        ('AckBytes', ctypes.c_uint8 * 8),
    ]



class ics_spy_messagew_bms(ctypes.Structure):
    _anonymous_  = ('Nameless20257', 'Nameless45821')
    _fields_ = [
        ('StatusBitField', ctypes.c_uint32),
        ('StatusBitField2', ctypes.c_uint32),
        ('TimeHardware', ctypes.c_uint32),
        ('TimeHardware2', ctypes.c_uint32),
        ('TimeSystem', ctypes.c_uint32),
        ('TimeSystem2', ctypes.c_uint32),
        ('TimeStampHardwareID', ctypes.c_uint8),
        ('TimeStampSystemID', ctypes.c_uint8),
        ('NetworkID', ctypes.c_uint8),
        ('NodeID', ctypes.c_uint8),
        ('Protocol', ctypes.c_uint8),
        ('MessagePieceID', ctypes.c_uint8),
        ('ExtraDataPtrEnabled', ctypes.c_uint8),
        ('NumberBytesHeader', ctypes.c_uint8),
        ('NumberBytesData', ctypes.c_uint8),
        ('NetworkID2', ctypes.c_uint8),
        ('DescriptionID', ctypes.c_uint16),
        ('Nameless20257', Nameless20257),
        ('Data', ctypes.c_uint8 * 8),
        ('Nameless45821', Nameless45821),
        ('ExtraDataPtr', ctypes.c_void_p),
        ('MiscData', ctypes.c_uint8),
        ('Reserved', ctypes.c_uint8 * 3),
    ]


_icsSpyMessagewBMS = ics_spy_messagew_bms
icsSpyMessagewBMS = ics_spy_messagew_bms

