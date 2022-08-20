""" 
Created on : 20/08/22 8:03 AM
@author : ds  
"""


def convert(l):
    return [str(i) for i in l]


print(convert([1, 2, 3]))


# using map
def convert(ns):
    return list(map(str, ns))