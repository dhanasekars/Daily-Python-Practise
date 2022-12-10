""" 
Created on : 10/12/22 5:15 AM
@author : ds
https://edabit.com/challenge/PgivAghJdMY7HM2pK
"""


from Dec_03_Four_Vectors import FourVectorOperators


class FourVectors2(FourVectorOperators):

    def __mul__(self, other):
        a = self.components
        if isinstance(other, FourVectors2):
            b = other.components
            return a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3]
        else:
            return FourVectors2([a[0] * other, a[1] * other, a[2] * other, a[3] * other])

    def __rmul__(self, other):
        return FourVectors2(self * other)

    def GetLength(self):
        return (abs(self * self))**0.5

