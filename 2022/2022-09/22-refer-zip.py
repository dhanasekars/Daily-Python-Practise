""" 
Created on : 22/09/22 5:46 AM
@author : ds  
"""


test_data = [5, 5, 10, 10, 15, 15, 20, 20]
total = 100


def interview(lst, tot):
    if tot > 120 or len(lst) < 8:
        return 'disqualified'
    else:
        if all(i <= 5 for i in lst[0:2]) and all(i <= 10 for i in lst[2:4]) \
                and all(i <= 15 for i in lst[4:6]) and all(i <= 20 for i in lst[6:8]):
            return "qualified"
        else:
            return 'disqualified'


# print(interview(test_data, total))

# Better way

# Define a list limit = [5,5,10,10,15,15,20,20] and use zip and compare input list with this.


def pythonic_interview(lst, tot):
    cut_off = [5, 5, 10, 10, 15, 15, 20, 20]
    return 'qualified' if all(i <= j for i, j in zip(lst, cut_off)) and tot <= 120 and len(lst) == 8 else 'disqualified'


print(pythonic_interview(test_data, total))
