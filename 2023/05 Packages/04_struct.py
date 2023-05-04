""" 
Created on : 27/04/23 7:21 am
@author : ds  
"""

import struct, os

with open('slick.bin', 'rb') as f:
    buf = f.read(132)
    print(buf)
    values = struct.unpack('33f', buf)
    print(values)
    print(f"the length of the values tuple is {len(values)}")


binary_data = b'\x2A\x00\x00\x00\x40\x09\x1E\xB8\x51\xEB\x85\x1F\xF9\x0B\x5B\xC0\x51\xEB\x85\x1F\xF9\x0B\x5B\xC0'
print(f"The length of the binary data is {len(binary_data)}")

values = struct.unpack('lid', binary_data)
print(values)

print(os.path.getsize('slick.bin'))

for kw in struct.__all__:
    print(kw)