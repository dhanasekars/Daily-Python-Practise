""" 
Created on : 21/01/23 4:48 AM
@author : ds
https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
"""

def kangaroo(x1, v1, x2, v2):
    """
    :param x1: starting position of kangaroo 1
    :param v1: speed of kangaroo 1
    :param x2: starting position of kangaroo 2
    :param v2: speed of kangaroo 2
    :return: YES or NO
    """
    if v1 <= v2:
        return 'NO'
    else:
        return 'YES' if (x2 - x1) % (v1 - v2) == 0 else 'NO'
