""" 
Created on : 23/02/23 5:58 AM
@author : ds  
"""
# find the greatest common divisor of two numbers

def gcd(a, b):
    """
    find the greatest common divisor of two numbers
    :param a:
    :param b:
    :return:
    """
    while b:
        a, b = b, a % b
    return a

