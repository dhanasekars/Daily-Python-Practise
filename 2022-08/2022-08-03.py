""" 
Created on : 03/08/22 5:14 PM
@author : ds  
"""
def mid(x):
    length = len(x)
    if length % 2 == 0:
        return
    else:
        return x[int(length/2)]



print(mid("helilo"))