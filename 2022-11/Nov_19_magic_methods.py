""" 
Created on : 18/11/22 1:25 PM
@author : ds  
"""
# Magic methods https://edabit.com/challenge/yKxKe74BBRDbRRPHx
# This is to learn magic methods and operator overloading
# https://rszalski.github.io/magicmethods/
# https://www.programiz.com/python-programming/operator-overloading
# No tests for this


class Number:
    def __init__(self, x=0):
        self.x = x

    def __str__(self):
        return f"{self.x}"

    def __repr__(self):
        return 'Number class overload examples'

    def __add__(self, other):
        output = self.x + other.x
        return Number(output)

    def __sub__(self, other):
        output = self.x - other.x
        return Number(output)

    def __mul__(self, other):
        output = self.x * other.x
        return Number(output)

    def __truediv__(self, other):
        output = self.x / other.x
        return Number(output)

    def __floordiv__(self, other):
        output = self.x // other.x
        return Number(output)

    def __eq__(self, other):
        return self.x == other.x

    def __float__(self):
        return float(self.x)


n1 = Number(2)
n2 = Number(4)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1//n2)
print(repr(n1))
print(float(n1))
print(n1 == n2)





