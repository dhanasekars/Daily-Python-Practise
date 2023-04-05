"""
Created on : 04/04/23 11:57 am
@author : ds  
"""


def is_it_prime(n):
    for i in range(2, int(n / 2) + 1):
        if i == 0:
            return False
        else:
            return True


