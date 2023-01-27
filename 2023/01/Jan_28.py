""" 
Created on : 28/01/23 5:07 AM
@author : ds  
"""
import math


def product_of_large_number(*lists):
    """
    Given any number of lists of integers,
    return the product of the largest values in each list without using any arithmetic operators (*, +, etc...)
    and without using a for-loop. Hint: use the standard library.

    :param lists:
    :return: integer
    """
    try:
        return math.prod([max(x) for x in lists])
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"
