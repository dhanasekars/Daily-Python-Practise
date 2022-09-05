""" 
Created on : 23/08/22 5:54 PM
@author : ds  
"""


def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        return False
    if n not in list2 and n not in list1:
        return False
    return True


print(list_xor(5, [5, 2, 3], [4, 3, 6]))

# using build in Xor


def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)