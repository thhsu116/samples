# Open a binary file and return its contect in byte array form
with open(binary_file, "rb") as binary_file_handle:
    data = binary_file_handle.read()

cmdString = "cmd " + ' '.join(x.encode('hex') for x in data)
cmd = ' '.join(x.encode('hex') for x in data)
byte_array = bytearray.fromhex(cmd)
