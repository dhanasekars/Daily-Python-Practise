""" 
Created on : 08 graphQL/07/23 9:12 am
@author : ds  
"""
test_data = [
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 0]
]


def tallest_skyscraper(lst):
    return sum(1 in row for row in lst)


print(tallest_skyscraper(test_data))

