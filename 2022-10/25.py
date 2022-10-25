""" 
Created on : 25/10/22 2:49 PM
@author : ds  
"""

data = (10, 15)


def collatz(a, b):
    counta, countb = 0, 0
    while a != 1:
        if a % 2 == 0:
            a = a / 2
            counta += 1
        else:
            a = 3*a + 1
            counta += 1

    while b != 1:
        if b % 2 == 0:
            b = b / 2
            countb += 1
        else:
            b = 3*b + 1
            countb += 1

    return "b" if counta > countb else "a"


print(collatz(10, 15))
