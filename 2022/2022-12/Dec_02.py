""" 
Created on : 02/12/22 4:55 AM
@author : ds  
"""

# https://edabit.com/challenge/cPxexgGxmCMi4kas8

class FourVector:
    """
    Four Vectors are vectors with four components that are used to describe relativistic physics.
    """

    def __init__(self, vectors=None):
        self.components = vectors if vectors else [0.0, 0.0, 0.0, 0.0]

    def GetComponents(self):
        return self.components

    def SetComponents(self, c):
        self.components = c

    def __str__(self):
        result = [round(item, 3) for item in self.components]
        return '{}'.format(str(tuple(result)))
