""" 
Created on : 06/03/23 2:24 PM
@author : ds  
"""

# clean up desktop

import os
import shutil

lis = []
i = 1
destination_dir = '/Users/DS/Desktop/Everything'
while os.path.exists(destination_dir):
    destination_dir += str(i)
    i += 1
os.makedirs(destination_dir)
lis = os.listdir('/Users/DS/Desktop')
for x in lis:
    if x == __file__:
        continue
    shutil.move('/Users/DS/Desktop/' + x, destination_dir)
