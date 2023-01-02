""" 
Created on : 02/01/23 6:29 AM
@author : ds  
"""

from Jan_02_random_walk import random_walk

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home =", abs(walk[0]) + abs(walk[1]))