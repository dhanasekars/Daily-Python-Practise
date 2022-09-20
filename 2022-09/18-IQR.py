""" 
Created on : 19/09/22 2:51 PM
@author : ds  
"""

test_data_odd = [-3.1, -3.8, -14, 23, 0]
test_data_even = [1, 2, 3, 4, 5]


def iqr(lst):
    lst = sorted(lst)
    midpoint = len(lst) // 2
    first_half = lst[:midpoint]
    if len(lst) % 2 == 0:
        second_half = lst[midpoint:]
    else:
        second_half = lst[midpoint+1:]
    if len(first_half) % 2 == 0:
        Q1 = (first_half[len(first_half) // 2] + first_half[(len(first_half) // 2) - 1]) / 2
    else:
        Q1 = first_half[(len(first_half) // 2)]
    if len(second_half) % 2 == 0:
        Q3 = (second_half[len(second_half) // 2] + second_half[(len(second_half) // 2 ) - 1]) / 2
    else:
        Q3 = (second_half[(len(second_half) // 2)])

    return Q3 - Q1


print(iqr(test_data_even))