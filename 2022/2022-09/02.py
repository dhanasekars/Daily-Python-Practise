""" 
Created on : 03 AutomateBoringStuffs/09/22 4:30 PM
@author : ds  
"""


def sum_odd_even(lst):
    # even_count, odd_count = 0, 0
    # for i in lst:
    #     if i % 2 == 0:
    #         even_count += i
    #     else:
    #         odd_count += i
    # return [even_count, odd_count]
    return [sum(i for i in lst if i % 2 == 0), sum(i for i in lst if i % 2 != 0)]


in_list = [-1, -2, -3, -4, -5, -6]
print(sum_odd_even(in_list))

