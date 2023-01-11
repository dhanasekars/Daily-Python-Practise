""" 
Created on : 10/10/22 5:32 AM
@author : ds  
"""
data = 12345


def digits_count(num, total=0):
    """
    function that will recursively count the number of digits of a number.
    Conversion of the number to a string is not allowed, thus, the approach is recursive.
    :param num:
    :param total: Count of digits
    :return: Integer - number of digits
    """
    num = abs(num)
    total = total + 1
    return total if num // 10 == 0 else digits_count(num // 10, total)


print(digits_count(data))