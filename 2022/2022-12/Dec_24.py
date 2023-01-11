""" 
Created on : 24/12/22 5:25 AM
@author : ds  
"""


def are_true(a, b):
    return 'both' if a and b else 'first' if a else 'second' if b else 'neither'


# def are_true(a, b):
# 	return {(1,1): 'both', (0,0): 'neither',
# 			(1,0): 'first', (0,1): 'second'}[a, b]


adder = lambda x: lambda y: x + y
add_2 = adder(2)
add_3 = adder(3)
add_5 = adder(5)
add_7 = adder(7)
add_11 = adder(11)
