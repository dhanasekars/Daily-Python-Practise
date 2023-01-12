""" 
Created on : 12/01/23 9:47 AM
@author : ds
https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
"""

def staircase(n):
    """
    It is a function that prints a staircase of size n.
    : param n: An integer
    :Print a staircase as described above.
    The function should not return a value.
    """
    for i in range(1, n+1):
        print(" " * (n - i) + "#"*i)


staircase(6)
