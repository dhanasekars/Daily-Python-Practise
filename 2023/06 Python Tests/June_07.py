""" 
Created on : 07/06/23 6:36 pm
@author : ds  
"""

import os
import os.path
def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)