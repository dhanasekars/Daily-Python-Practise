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
        self.vectors = [0.0, 0.0, 0.0, 0.0] if vectors is None else vectors

    def SetComponents(self, c):
        self.vectors = c

    def GetComponents(self):
        return self.vectors

    def __str__(self):
        result = [round(item, 3) for item in self.vectors]
        return '{}'.format(str(tuple(result)))
