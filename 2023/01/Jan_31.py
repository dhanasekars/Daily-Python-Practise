""" 
Created on : 31/01/23 4:48 AM
@author : ds  
"""

def stringcap(string):
    """
    Given a string, return True if the last letter is capitalized and False otherwise..
    :param string: string
    :return: Bool
    """
    try:
        return string[-1].isupper()
    except IndexError:
        return "Empty String"
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"

def common_char(s1, s2):
    """
    Given two strings, return a list of the common characters between them.
    :param s1: string
    :param s2: string
    :return: list
    """
    try:
        return set(sorted(set(s1) & set(s2)))
    except TypeError:
        return "List contains non-numeric values."
    except Exception as e:
        return f"Error: {e}"


print(common_char("abc", "def"))
