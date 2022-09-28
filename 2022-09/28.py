"""
Created on : 27/09/22 3:53 PM
@author : ds
"""

test_data = [75.8, 696, 14.8, 177.6, 0.81]


def least_squares_line(lst):
    m = lst[-1] * (lst[3] / lst[2])
    b = lst[1] - m * lst[0]
    return f"{round(b,2)} + {round(m,2)}x"


print(least_squares_line(test_data))