""" 
Created on : 24/04/23 11:43 am
@author : ds  
"""

from PIL import Image
maze = Image.open("maze.png")
w, h = maze.size


for i in range(w):
    print(maze.getpixel((i, h-1)))


# http://www.pythonchallenge.com/pc/hex/lake.html

