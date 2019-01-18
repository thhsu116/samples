import pythoncom
from win32com.client import VARIANT

# converting byte array to VT_ARRAY and sent to target over win32 handles
v = VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_UI1, byte_array)  # VT_ARRAY: A SAFEARRAY pointer, VT_UI1: An unsigned character
resp = qpst_port.SendCommand(v, 2000)
resp_hex_str = " ".join("%02x" % b for b in bytearray(resp))

# construct a bytearray
import struct
test = bytearray.fromhex('00 00 00 00')  # reserved
test += struct.pack('<I', 0)  # a little-endian unsigned int data field
