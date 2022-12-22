""" 
Created on : 22/12/22 5:24 AM
@author : ds  
"""

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.51)+1))
