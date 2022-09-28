""" 
Created on : 27/09/22 5:18 AM
@author : ds  
"""

test_data = [44, 45, 1]
test_data1 = [42, 3, 6]


def consecutive_combo(lst1, lst2):
    flag = False
    lst = sorted(lst1 + lst2)
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] == 1:
            flag = True
        else:
            return False
    return flag


def pythonic_combo(lst1, lst2):
    lst = sorted(lst1 + lst2)
    return all(lst[i + 1] - lst[i] == 1 for i in range(len(lst) - 1))


print(pythonic_combo(test_data, test_data1))
