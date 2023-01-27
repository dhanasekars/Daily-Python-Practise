""" 
Created on : 27/01/23 4:42 AM
@author : ds  
"""

def single_largest_value(*lists):
    """
    Given a list of integers. Return the list with single largest value.
    ----------
    list : a list of integers

    Returns
    -------
    a list
    """
    try:
        return max(lists, key=lambda x: max(x))
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"

def max_values_list(*lists):
    """
    Given a list of integers. Return the list of max values from the lists.
    :param lists:
    :return: a list of max values sorted in descending order
    """
    try:
        return sorted([max(x) for x in lists], reverse=True)
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"

def max_position_list(*lists):
    """
    Given a list of integers. Return the list of max value at position from the lists.
    Add a condition to check if length of lists are equal. If not throw an error.
    :param lists:
    :return: a list of max values for each position
    """
    try:
        return [max(x) for x in zip(*lists)]
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"