""" 
Created on : 18/09/22 7:24 PM
@author : ds  
"""
import math

test_data = [8, 4, 14, 16, 8]

# sorted = [1,2,3,4,5]


def sd(lst):
    data_point = len(lst)
    sum_of_data_point = sum(lst)
    mean = sum_of_data_point / data_point
    sample_variance = sum([(mean - i)**2 for i in lst]) / (data_point - 1)
    variance = sum([(mean - i)**2 for i in lst]) / data_point
    SD = math.sqrt(variance)
    sample_SD = math.sqrt(sample_variance)
    # return round(SD, 2)
    return mean, SD


print(sd(test_data))