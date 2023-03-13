""" 
Created on : 13/03/23 9:59 am
@author : ds  
"""

from config import Obsidian
import os

# Get all zero KB files in a given directory

for (root, dirs, file) in os.walk(Obsidian.folder):
    for f in file:
        if os.stat(Obsidian.folder+f).st_size == 0:
            print(f)
