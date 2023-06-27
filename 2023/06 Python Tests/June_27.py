""" 
Created on : 27/06/23 9:59 am
@author : ds  
"""

from random import shuffle

x = [i for i in range(1, 10)]
y = list("abcdefghijklmnopqrstuvwxyz")
shuffle(x)

print(dict(zip(x, y)))
