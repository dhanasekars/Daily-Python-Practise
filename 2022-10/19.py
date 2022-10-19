""" 
Created on : 19/10/22 6:18 AM
@author : ds  
"""

data = {"piano": "200"}


def convert_to_number(dictionary):
    """
    convert dict value from string to numbers
    :param dictionary: Key value pair both are stings
    :return: dictionary key value pair, key being string and value as number
    """
    # solved using dict comprehension
    return {k: int(v) for (k, v) in dictionary.items()}


print(convert_to_number(data))