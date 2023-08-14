""" 
Created on : 14/08/23 5:36 pm
@author : ds  
"""
def calculate():
    total = 0
    a = 0
    b = 1

    while a < 1000000:
        if a % 2 == 0:
            total = total + a
        a, b = b, a + b

    return total


print(calculate())