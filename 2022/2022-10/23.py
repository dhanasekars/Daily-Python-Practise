""" 
Created on : 25/10/22 2:22 PM
@author : ds  
"""
import math

import numpy

data = 100


def fact_of_fact(n):
    # output = 1
    # for i in range(n, 1, -1):
    #     output = output * math.factorial(i)
    return numpy.prod([math.factorial(i) for i in range(n, 1, -1)])


print(fact_of_fact(data))

