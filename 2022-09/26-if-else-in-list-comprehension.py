""" 
Created on : 26/09/22 2:31 PM
@author : ds  
"""

test_data = [4, 1, 4]


def show_the_love(lst):
    total = min(lst) + sum([i*0.25 for i in lst if i is not min(lst)])
    new_lst = [i*0.75 if i is not min(lst) else total for i in lst]
    return new_lst


print(show_the_love(test_data))