""" 
Created on : 12/08/22 12:35 PM
@author : ds  
"""

def largest_difference(l):
    sorted_l = sorted(l)
    return sorted_l[-1] - sorted_l[0]

print(largest_difference([1,2,3]))

# better solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)