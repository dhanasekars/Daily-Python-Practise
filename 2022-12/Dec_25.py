""" 
Created on : 25/12/22 5:26 AM
@author : ds
https://edabit.com/challenge/AaSXX4SKNdZ7mgqK7
"""

def first_one(a, b=None, c=None, d=None):
    return a or b or c or d or "not found"

def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    hgst = find_highest(lst[1:])
    return hgst if hgst >= lst[0] else lst[0]