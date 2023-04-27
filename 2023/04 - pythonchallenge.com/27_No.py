""" 
Created on : 27/04/23 7:03 am
@author : ds  
"""

from PIL import Image
import keyword

im = Image.open('zigzag.gif')
palette = im.getpalette()[::3]
# print(bytes(palette))
raw = im.tobytes()
table = bytes.maketrans(bytes([i for i in range(256)]), bytes(palette))
print(raw.translate(table))

# http://www.pythonchallenge.com/pc/ring/bell.html
#
# username: repeat
# password: switch