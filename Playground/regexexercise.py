""" 
Created on : 03/02/23 1:14 PM
@author : ds  
"""
import re

def count_match(string, pattern):
    """
    Return the number of times the pattern appears in the string.
    :param string:
    :param pattern:
    :return: int
    """
    return len(re.findall(pattern, string))
