""" 
Created on : 08/08/22 5:14 PM
@author : ds  
"""


def add_dots(a):
    chars = list(a)
    b = chars[0] + "."
    for i in chars[1:]:
        b = b + i + "."
    return b[:-1]

# short way learned looking at the solution


def add_dots_smart_way(a):
    return ".".join(a)


def remove_dots(a):
    return a.replace(".", "")

