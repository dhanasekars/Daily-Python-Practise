""" 
Created on : 19/09/22 3:23 PM
@author : ds  
"""

test_data = 5


def is_disarium(n):
    total = 0
    for i, d in enumerate(list(str(n)), start=1):
        total = total + pow(int(d), int(i))
    return n == total


print(is_disarium(test_data))
