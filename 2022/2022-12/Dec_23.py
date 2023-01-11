""" 
Created on : 23/12/22 6:16 AM
@author : ds
https://edabit.com/challenge/2TdPmSpLpa8NWh6m9
https://edabit.com/challenge/JQHEYvFJPv4eSAjox
"""

a = [3, 3, 3]
b = [1, 2, 3]


def equilibrium(x):
    return "positive" if x > 0 else "negative" if x < 0 else True


def not_share(lst1, lst2):
    return all(i not in lst2 for i in lst1)

# More pythonic solution
# return not set(lst1) & set(lst2)
