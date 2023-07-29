""" 
Created on : 29/07/23 1:19 pm
@author : ds  
"""
from math import pi


def area_of_circle(rad):
    if rad < 0:
        raise ValueError
    if type(rad) not in [int, float]:
        raise TypeError

    return pi * (rad ** 2)

# Test Function

# radii = [ 2, 0, -3, 2+5j, True, "helloooo" ]
# message = "Area of circles with r = {radius} is {area}"
# for r in radii:
#     A = area_of_circle(r)
#     print(f"Area of circles with r = {r} is {A}")
