""" 
Created on : 03/09/22 3:36 PM
@author : ds  
"""


def is_leap(year):
    return (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)


print(is_leap(1800))
