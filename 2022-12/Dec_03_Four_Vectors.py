""" 
Created on : 03/12/22 4:40 AM
@author : ds  
"""

from Dec_02 import FourVector


class FourVectorOperators(FourVector):

    def __add__(self, other):
        return FourVector([self.vectors[item] + other.vectors[item] for item in range(4)])

    def __sub__(self, other):
        output = [self.vectors[item] - other.vectors[item] for item in range(4)]
        return FourVector(output)

    def __eq__(self, other):
        return all([self.vectors[item] == other.vectors[item] for item in range(4)])

# Learnings

# Return as object for the operator overload so this can used for more than two instances.
# v2 = FourVector([1, 0, 0, 1])
# v3 = FourVector([1, 0, 1, 0])
# v4 = FourVector([-1, 4, 1, 2])
# print(v2 + v3 - v4)
