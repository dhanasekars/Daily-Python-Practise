""" 
Created on : 25/10/22 2:49 PM
@author : ds  
"""

data = (10, 15)


def steps(x, count=0):
    while x != 1:
        count += 1
        # This loop gets executed if it is odd.
        # Since for even the output is zero. Zero is falsy value in python
        if x % 2:
            x = 3 * x + 1
        else:
            x //= 2
    return count


def collatz(a, b):
    return "b" if steps(a) > steps(b) else "a"


print(collatz(10, 15))
