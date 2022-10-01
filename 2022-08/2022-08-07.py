""" 
Created on : 07/08/22 4:43 PM
@author : ds  
"""


def double_letters(a):
    for i in range(len(a)):
        if i < len(a)-1:
            if a[i] == a[i+1]:
                return True
    return False


print(double_letters("Test.t"))

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])