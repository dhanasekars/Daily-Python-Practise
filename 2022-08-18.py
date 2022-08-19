""" 
Created on : 18/08/22 5:54 PM
@author : ds  
"""


def all_equal(l):
    flag = ""
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            flag = True
        else:
            return False
    return flag


print(all_equal([5, 5, 5]))


# can use two loop
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True

