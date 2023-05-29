""" 
Created on : 29/05/23 11:33 am
@author : ds  
"""

import glob

# find all py files in the current directory

py_files = glob.glob("*.py")
print(py_files)
print(glob.__all__)


py_ifiles = glob.iglob("*.py")
for file in py_ifiles:
    print(file)

