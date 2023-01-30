""" 
Created on : 30/01/23 9:33 AM
@author : ds  
"""

def odd_even_difference(lst):
    """
    Given a list of integers, return the difference between the sum of the even integers and the sum of the odd integers.

    :param lst: list of integers
    :return: integer
    """
    try:
        return abs(sum([x for x in lst if x % 2 == 0]) - sum([x for x in lst if x % 2 != 0]))
    except TypeError:
        return "List contains non-numeric values."
    except ValueError:
        return "Empty list"
    except Exception as e:
        return f"Error: {e}"
