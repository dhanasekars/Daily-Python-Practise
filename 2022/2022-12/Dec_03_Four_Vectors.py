""" 
Created on : 03 AutomateBoringStuffs/12/22 4:40 AM
@author : ds  
"""

from Dec_02 import FourVector


class FourVectorOperators(FourVector):

    def __add__(self, other):
        return FourVectorOperators([self.components[item] + other.components[item] for item in range(4)])

    def __sub__(self, other):
        output = [self.components[item] - other.components[item] for item in range(4)]
        return FourVectorOperators(output)

    def __eq__(self, other):
        return all([self.components[item] == other.components[item] for item in range(4)])


# Learnings

# Return as object for the operator overload so this can used for more than two instances.
# v2 = FourVectorOperators([1, 0, 0, 1])
# v3 = FourVectorOperators([1, 0, 1, 0])
# v4 = FourVectorOperators([-1, 4, 1, 2])
# print(v2 + v3)
