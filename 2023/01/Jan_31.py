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




print(stringcap("HellO"))