""" 
Created on : 28/10/22 5:27 AM
@author : ds  
"""
import re
data = "a very largest appliance"


def vowel_links(txt):
    """
    Given a sentence as txt, return True if any two adjacent words have this property:
    One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
    :param txt: String
    :return: Bool
    """
    return bool(re.search('[aeiou] [aeiou]', txt))


print(vowel_links(data))