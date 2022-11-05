""" 
Created on : 05/11/22 6:04 AM
@author : ds  
"""


def histogram(lst, char):
    return '\n'.join([char*i for i in lst])


print(histogram([6, 2, 15, 3], "="))