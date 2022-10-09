""" 
Created on : 09/10/22 5:40 AM
@author : ds  
"""
import math

data = [[15, 7], [5, 22], [11, 1]]


def perimeter(lst):
    """
    Function that takes the coordinates of three points in the form of a 2d array
    :param lst:the vertices of a triangle on a two-dimensional plane.
    :return:returns the perimeter of the triangle.
    """

    one = math.sqrt(pow(lst[0][0] - lst[1][0], 2) + pow(lst[0][1] - lst[1][1], 2))
    two = math.sqrt(pow(lst[1][0] - lst[2][0], 2) + pow(lst[1][1] - lst[2][1], 2))
    three = math.sqrt(pow(lst[0][0] - lst[2][0], 2) + pow(lst[0][1] - lst[2][1], 2))

    return round(one + two + three, 2)


print(perimeter(data))
