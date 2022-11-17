""" 
Created on : 16/11/22 6:11 AM
@author : ds  
"""

# https://edabit.com/challenge/nC7iHBbN8FEPy2EJ2

from math import pi


class Circle:
    """
    Your task is to create a Circle constructor that creates a circle with a radius
    provided by an argument. The circles constructed must have two getters getArea() (PI*r^2)
    and getPerimeter() (2*PI*r) which give both respective areas and perimeter (circumference).
    """

    def __init__(self, radius=0.0):
        self.radius = radius

    def getArea(self):
        return pi*self.radius*self.radius

    def getPerimeter(self):
        return 2 * pi * self.radius


circle = Circle(11)
circy = Circle(4.44)
print(circle.getArea())
print(circy.getPerimeter())




