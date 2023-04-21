""" 
Created on : 21/04/23 6:47 am
@author : ds  
"""

import zlib, bz2


data = b'x\x9c This is a byte string'
result = ''

# check the compression algorithm used, it is either zlib or bz2
while True:
    if data.startswith(b'x\x9c'):
        data = zlib.decompress(data)
        result += ' '
    elif data.startswith(b'BZh'):
        data = bz2.decompress(data)
        result += "#"
    elif data.endswith(b'\x9cx'):
        data = data[::-1]
        result += '\n'
    else:
        break

print(data)

# since the previous level is unsolved, unable to get the zip file for this challenge
#  http://www.pythonchallenge.com/pc/hex/copper.html

