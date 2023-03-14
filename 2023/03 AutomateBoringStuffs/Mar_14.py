""" 
Created on : 14/03/23 5:47 am
@author : ds  
"""

from config import Obsidian
import os

count = 0

# Get all files less than or equal to one byte in a given directory

for (root, dirs, file) in os.walk(Obsidian.folder):
    for f in file:
        if os.stat(Obsidian.folder+f).st_size <= 1:
            print(f)
            os.remove(Obsidian.folder+f)
            count = count + 1

if count == 0:
    print("No zero KB files found")
elif count == 1:
    print("One file removed")
else:
    print("{} zero KB files deleted".format(count))
