""" 
Created on : 01/10/22 5:44 AM
@author : ds  
"""
test_data = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sock_merchant(lst):
    """
    Given a list of integers representing the color of each sock,
    determine how many pairs of socks with matching colors there are.
    For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2].
    There is one pair of color 1 and one of color 2.
    There are three odd socks left, one of each color.
    The number of pairs is 2.
    :param lst:
    :return: An integer
    """
    # Use set to get unique values in the lst
    # for each item in the set, count the total of the number
    # Taking two mod for the count will return pairs
    # Summing the mod of the count gives total pair
    # This is done using list comprehension

    return sum([lst.count(i) // 2 for i in set(lst)])


print(sock_merchant(test_data))