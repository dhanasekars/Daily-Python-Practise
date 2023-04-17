""" 
Created on : 16/04/23 12:53 pm
@author : ds  
"""

from PIL import Image, ImageChops
import numpy as np


# my_list = image.histogram()
# pink = [x for x in my_list if x % image.height == 0 and x != 0]
# print(my_list.index(pink[0]))
#
# tmp = image.copy()
# tmp.frombytes(bytes([195] * (tmp.height * tmp.width)))
# tmp.show()

image = Image.open("mozart.gif")
shifted = [bytes(np.roll(row, -row.tolist().index(195)).tolist()) for row in np.array(image)]
Image.frombytes('P', image.size, b"".join(shifted)).show()

#  Solution is not working, there is an issue creating an image frombytes.
# The solution is 'romance'

# http://www.pythonchallenge.com/pc/return/romance.html