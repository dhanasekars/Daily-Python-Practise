""" 
Created on : 10/09/22 9:39 AM
@author : ds  
"""

test_data = [
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 0, 0]
]


def tallest_skyscraper(lst):
    for i in lst:
        for j in i:
            if j == 1:
                return len(lst) - lst.index(i)
    return 0


print(tallest_skyscraper(test_data))

# Pythonic way

# return sum(1 in R for R in lst)
