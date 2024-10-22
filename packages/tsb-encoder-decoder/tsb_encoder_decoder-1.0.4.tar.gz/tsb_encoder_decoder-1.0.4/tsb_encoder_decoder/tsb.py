from cobs import cobs
import crcmod.predefined
from typing import Tuple, Union

'''
e.g.: 
from tsb_encoder_decoder import tsb
tsb_msg = tsb.encode(0x01, tsb.TSB_TYPE_TEXT, b"Hello, world!")
channel, tsb_type, payload = tsb.decode(tsb_msg) 
print(channel, tsb_type, payload)
'''

TSB_TYPE_RAW =              0x01
TSB_TYPE_TEXT =             0x02
TSB_TYPE_ENVELOOP =         0x05
TSB_TYPE_ATCMD =            0x09
TSB_TYPE_BEACONLINE =       0x11
TSB_TYPE_BLUETOOTH_HCI =    0x15
TSB_TYPE_COAP =             0x21
TSB_TYPE_JSON =             0x30
TSB_TYPE_CBOR =             0x30
TSB_TYPE_SENML =            0x6E
TSB_TYPE_SENSML =           0x6F
TSB_TYPE_CAN =              0x41
TSB_TYPE_TEST =             0x70
TSB_TYPE_INFLUX =           0x75
TSB_TYPE_LOG =              0x7D
TSB_TYPE_WARNING =          0x7E
TSB_TYPE_ERROR =            0x7F

class TSBEncoderDecoder(Exception):
    pass
    

def encode(channel: int, tsb_type: int, payload: bytes) -> bytes:
    """Encodes a TSB message.

    Args:
        channel: The TSB channel.
        tsb_type: The TSB type.
        payload: The TSB payload.

    Returns:
        The encoded TSB message.
    """

    # Validate input
    if channel < 0 or channel > 255:
        raise ValueError("Invalid channel value")
    if tsb_type < 0 or tsb_type > 255:
        raise ValueError("Invalid TSB type value")

    raw = channel.to_bytes(1, 'big') + tsb_type.to_bytes(1, 'big') + payload
    crc16 = crcmod.predefined.Crc('modbus')
    crc16.update(raw)
    raw = raw + crc16.crcValue.to_bytes(2, 'little')
    tsb_msg = cobs.encode(raw) + b'\x00'
    return tsb_msg

def decode(tsb_msg: bytes) -> Union[Tuple[int, int, bytes], bool]:
    """Decodes a TSB message.

    Args:
        tsb_msg: The encoded TSB message.

    Returns:
        A tuple containing the channel, type, and payload of the decoded TSB message, or False if the decoding failed.
    """

    tsb_length = len(tsb_msg)
    if tsb_length < 6:
        return False

    raw = cobs.decode(tsb_msg[0:(tsb_length - 1)])
    crc16 = crcmod.predefined.Crc('modbus')
    crc16.update(raw[0:(tsb_length - 4)])
    crc_calc = crc16.crcValue.to_bytes(2, 'little')
    crc_msg = raw[(tsb_length - 4):(tsb_length - 2)]
    if crc_calc != crc_msg:
        raise ValueError("CRC mismatch")

    return raw[0], raw[1], raw[2:(tsb_length - 4)]