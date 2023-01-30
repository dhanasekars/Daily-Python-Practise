""" 
Created on : 29/01/23 4:48 AM
@author : ds  
"""


def sorting_list(*lists):
    """
    :param: lists: a tuple of lists of integers
    :return: list
    """
    appended_list = []
    try:
        for lst in lists:
            appended_list += lst
        return sorted(appended_list)
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"
