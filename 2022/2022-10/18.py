""" 
Created on : 18/10/22 5:41 AM
@author : ds  
"""
from collections import Counter
data = ["cow", "pig", "cow", "cow"]


def pluralize(lst):
    """
    Given a list of words in the singular form,
    return a set of those words in the plural form if they appear more than once in the list
    :param lst: List of names
    :return: Set
    """
    # Set comprehension is used on the collections Counter dictionary
    # Counter is a container that will hold the count of each of the elements present in the container.
    # The counter is a sub-class available inside the dictionary class.
    # https://docs.python.org/3/library/collections.html
    # Another way to solve is using count method lst.count(i)
    return {k if v == 1 else k+'s' for k, v in Counter(lst).items()}


print(pluralize(data))