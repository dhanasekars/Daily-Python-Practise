""" 
Created on : 06/09/22 3:31 PM
@author : ds  
"""


def number_length(num, count=1):
    num = num // 10
    if num != 0:
        return number_length(num, count + 1)
    else:
        return count


print(number_length(4545345430))