""" 
Created on : 24/01/23 8:57 AM
@author : ds
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
"""

def catAndMouse(x, y, z):
    """
    :param x: integer, Cat A's position
    :param y: integer, Cat B's position
    :param z: integer, Mouse C's position
    :return: string
    """
    if abs(x - z) < abs(y - z):
        return 'Cat A'
    elif abs(x - z) > abs(y - z):
        return 'Cat B'
    else:
        return 'Mouse C'


