""" 
Created on : 05/10/22 6:45 AM
@author : ds  
"""

data = 8


def pentagonal(num):
    """

    :param num: takes a positive integer num
    and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
    :return: An int - Number of dots around pentagon on the nth iteration
    """
    # formula is 1 + 5 + 10 + 15 + ...
    # which is = 1 + 5(1 + 2 + 3 +... n - 1)
    # To sum n natural numbers use the formula n*(n+1) / 2. Here n = n -1
    # so formula to sum is n*(n-1) /2

    return int((num * (num-1) / 2) * 5 + 1)


print(pentagonal(data))