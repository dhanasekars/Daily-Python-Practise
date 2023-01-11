""" 
Created on : 11/11/22 5:40 AM
@author : ds  
"""


def multiplication_table(n):
    """
    Your task, is to create N x N multiplication table, of size n provided in parameter.
    For example, when n is 5, the multiplication table is:
    1, 2, 3, 4, 5
    2, 4, 6, 8, 10
    3, 6, 9, 12, 15
    4, 8, 12, 16, 20
    5, 10, 15, 20, 25
    :param n: int
    :return: list of lists
    """
    return [[i*j for j in range(1, n+1)] for i in range(1, n+1)]


print(multiplication_table(5))
