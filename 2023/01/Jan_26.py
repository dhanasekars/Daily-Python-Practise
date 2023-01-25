""" 
Created on : 26/01/23 5:21 AM
@author : ds  
"""

def largestsumlist(*lists):
    """
    Given a list of lists. Return the list that has largest sum.
    Parameters
    ----------
    lists : a list of lists
    Returns
    -------
    an integer
    """
    print(lists)
    try:
        return max(lists, key=sum)
    except ValueError:
        return "Empty list"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"

