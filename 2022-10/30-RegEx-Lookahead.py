""" 
Created on : 30/10/22 9:51 AM
@author : ds  
"""

import re
data = "Texas = no, California =yes, Florida = yes, Michigan = no"


def positive_lookahead(txt):
    return re.findall(r'\w+(?= = yes)', txt)


def negative_lookahead(txt):
    return re.findall(r'(\w+) (?!= yes)', txt)


lst = ["tall height", "tall height", "short height", "medium height", "tall height"]


def positive_lookbehind(txt):
    return len(re.findall(r'(?<=tall)', ",".join(txt)))


print(positive_lookbehind(lst))

