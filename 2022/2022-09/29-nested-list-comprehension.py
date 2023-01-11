""" 
Created on : 29/09/22 5:19 AM
@author : ds  
"""

test_data = 74


def is_disarium(n):
    return sum([pow(j, i) for i, j in enumerate([int(i) for i in list(str(n))], start=1)]) == n
    # [int(i) for i in list(str(n))] --> convert the input number to a list of individual digits
    # then use that list and do a list comprehension to raise to its position's power using enumerate


print(is_disarium(test_data))



