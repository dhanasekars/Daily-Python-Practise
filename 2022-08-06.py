""" 
Created on : 06/08/22 12:36 PM
@author : ds  
"""


def only_ints(a, b):
    return type(a) == int and type(b) == int


print(only_ints('t', 5))
