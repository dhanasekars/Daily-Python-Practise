""" 
Created on : 12/10/22 5:47 AM
@author : ds  
"""
import numpy as np

data = 6


def id_mtrx(n):
    if n >= 0 and n == int(n):
        return np.identity(n)
    elif n < 0 and n == int(n):
        idm = np.identity(abs(n))
        return np.rot90(idm)
    else:
        return "Error"


print(id_mtrx(data))
