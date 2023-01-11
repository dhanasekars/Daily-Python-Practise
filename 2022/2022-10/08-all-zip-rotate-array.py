""" 
Created on : 08/10/22 6:38 AM
@author : ds  
"""
import numpy as np

data1 = [[1, 2, 3, 2, 1, 1],
         [2, 4, 4, 3, 2, 2],
         [5, 5, 5, 10, 4, 4],
         [6, 6, 7, 6, 5, 5]]

data2 = [
    [2, 0, 0],
    [1, 1, 1],
    [2, 2, 2]]


def can_see_stage(seats):
    """
    Create a function that determines whether each seat can "see" the front-stage.
    A number can "see" the front-stage if it is strictly greater than the number before it.
    :param: seats List of lists with seat numbers
    :return: Boolean
    """
    rotated = list(zip(*seats[::-1]))
    # rotate an array https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    # used set to check if two elements in a list are same, that also means other person cannot see.
    # The above set logic is to check for strictly greater than condition.
    # then compared a descending-ly sorted list to itself to check if the seats are in expected order.
    return all([len(set(i)) == len(i) for i in rotated]) and all([list(i) == sorted(i, reverse=True) for i in rotated])


print(can_see_stage([
    [1, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]))


# Better pythonic solution

def can_see_stage_pythonic(seats):
    return all(sorted(set(row)) == list(row) for row in zip(*seats))
