""" 
Created on : 21/08/22 8:54 PM
@author : ds  
"""

# implement a zip function


x = [0, 1, 2, 3]
y = [5, 6, 7, 8]


def zap(a, b):
    result = []
    for i in range(len(a)):
        tup = (a[i], b[i])
        result.append(tup)

    return result


# using list comprehension

def zap_com(a, b):
    return [(a[i], b[i]) for i in range(len(a))]


print(zap_com(x, y))
