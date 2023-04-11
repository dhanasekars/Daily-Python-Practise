""" 
Created on : 11/04/23 9:06 am
@author : ds  
"""

from PIL import Image

im = Image.open('cave.jpg')
(w, h) = im.size

even = Image.new('RGB', ( w // 2, h // 2))
odd = Image.new('RGB', ( w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i, j))
        if ( i + j) % 2 == 1:
            odd.putpixel( (i // 2, j // 2), p)
        else:
            even.putpixel( (i // 2, j // 2), p)

even.show("even")
odd.show("odd")
even.save("even.jpg")


# evil
# http://www.pythonchallenge.com/pc/return/evil.html
