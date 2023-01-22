""" 
Created on : 23/01/23 4:41 AM
@author : ds
https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
"""


def dayOfProgrammer(year):
    """
    :param year: integer
    :return: string
    """
    if year == 1918:
        return '26.09.1918'
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return f'12.09.{year}'
    else:
        return f'13.09.{year}'


# Logic to find leap year:
# if year is not divisible by 4 then it is a common year.
# else if year is not divisible by 100 then it is a leap year.
# else if year is not divisible by 400 then it is a common year.
# else it is a leap year.

# def is_leapyear(n):
#     if n % 4 == 0 and  (n % 100 == 0 or n % 400 == 0):
#         return True
#     else:
#         return False


