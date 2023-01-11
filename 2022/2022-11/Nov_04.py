""" 
Created on : 04/11/22 5:50 AM
@author : ds  
"""
from math import pi, sin


def circle(n):
    """
    A circle has a circumference of 100 meters. A regular polygon, let's say a square,
    inscribed inside this circle has a perimeter of about 90 meters.
    As you increase the number of sides of the regular polygon,
    it's perimeter will become arbitrarily close to 100 meters.
    Write a function whose argument is the number of sides of the inscribed regular polygon.
    The function returns the polygon's perimeter. Round your answer to 3 decimal places.
    :param n: Number of sides of polygon
    :return: integer - area of polygon
    """
    r = round(100 / (2 * pi), 4)
    theta = (360 / n * pi) / 180
    return round(n * 2 * r * sin(theta/2), 3)


print(circle(12))
