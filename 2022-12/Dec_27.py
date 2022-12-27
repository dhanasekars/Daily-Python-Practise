""" 
Created on : 27/12/22 5:28 AM
@author : ds
"""


def list_of_multiples(num, length):
    """
    function that takes two numbers as arguments (num, length) and returns a list of multiples of num
    until the list length reaches length.
    :param num: integer
    :param length: integer
    :return: list of integers
    """
    return [num * i for i in range(1, length + 1)]


def add(n1, n2):
    """
    function that takes two number strings and returns their sum as a string.
    :param n1: String
    :param n2: String
    :return: Sum as string
    """
    try:
        return str(int(n1) + int(n2))
    except (TypeError, ValueError):
        return "Invalid Operation"
