""" 
Created on : 07/04/23 8:43 am
@author : ds  
"""
import re

from PIL import Image

#  http://www.pythonchallenge.com/pc/def/oxygen.html

# smarty

# Grey scale in the image is the clue


img = Image.open("07_oxygen.png")

row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]

ords = [r for r, g, b, a in row if r == g == b][::7]
# print("".join(map(chr, ords)))

# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

code = re.findall("\d+", "".join(map(chr, ords)))
print(code)

print(''.join(chr(int(num)) for num in code))

# integrity

# http://www.pythonchallenge.com/pc/def/integrity.html