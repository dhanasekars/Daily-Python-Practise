""" 
Created on : 25/01/23 4:36 AM
@author : ds
"""


def exercise_1(a_list):
    """
    Given a list of integers. Return the difference between the largest and smallest values.
    Parameters
    ----------
    a_list : a list of numbers

    Returns
    -------
    an integer
    """
    try:
        return max(a_list) - min(a_list)
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"

