""" 
Created on : 10/07/23 5:38 pm
@author : ds  
"""

def add(n1, n2):
    if (n1 in ["", None]) or (n2 in ["", None]):
        return "Invalid Operation"
    else:
        return str(int(n1) + int(n2))


print(add("111", None))