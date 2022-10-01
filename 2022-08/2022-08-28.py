""" 
Created on : 28/08/22 6:27 PM
@author : ds  
"""


def total_overs(b):
    overs = b//6
    balls = b % 6
    if balls != 0:
        return f"{overs}.{balls}"
    else:
        return f"{overs}"


print(total_overs(66))

