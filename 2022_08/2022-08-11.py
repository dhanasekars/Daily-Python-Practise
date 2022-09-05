""" 
Created on : 11/08/22 5:23 PM
@author : ds  
"""


def flatten(a):
    j = []
    for i in a:
        j.extend(i)
    return j



print(flatten([[1,2,3],[4,5,6]]))