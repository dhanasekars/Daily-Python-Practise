""" 
Created on : 20/09/22 11:25 AM
@author : ds  
"""

test_data = [5, 9, 5, 5, 7, 11]


def mad(lst):
    sum_of_data_points = sum(lst)
    data_points = len(lst)
    mean = sum_of_data_points / data_points
    total_distance_from_mean = sum([abs(i - mean) for i in lst])

    return round(total_distance_from_mean / data_points, 2)



print(mad(test_data))