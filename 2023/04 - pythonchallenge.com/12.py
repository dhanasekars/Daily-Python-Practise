""" 
Created on : 12/04/23 10:29 am
@author : ds  
"""
import io

from PIL import Image

data = open("../evil2.gfx", "rb").read()
for i in range(5):
    image_bytes = data[i::5]
    im = Image.open(io.BytesIO(image_bytes))
    im.show()

# $ curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg

# http://www.pythonchallenge.com/pc/return/disproportional.html