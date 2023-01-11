""" 
Created on : 08/09/22 11:45 AM
@author : ds  
"""


sample = {"z": "q", "w": "f"}


def invert(dct):
    return {value: key for (key, value) in dct.items()}


print(invert({ "zebra": "koala", "horse": "camel" }))

