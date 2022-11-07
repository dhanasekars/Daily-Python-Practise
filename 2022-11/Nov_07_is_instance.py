""" 
Created on : 07/11/22 5:36 AM
@author : ds  
"""

data = [1, 2, 3]


def num_of_sublists(lst):
    return sum([isinstance(i, list) for i in lst])


print(num_of_sublists(data))

# Smart solution
# return str(lst).count('[') - 1
# The above is to count number of open square brackets -1
