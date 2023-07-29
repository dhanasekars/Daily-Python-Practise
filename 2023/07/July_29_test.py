""" 
Created on : 29/07/23 1:25 pm
@author : ds  
"""

from July_29 import area_of_circle
import unittest
from math import pi


class TestAreaOfCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(2.1), pi * 2.1 ** 2)

    def test_value(self):
        self.assertRaises(ValueError, area_of_circle, -4)

    def test_type(self):
        self.assertRaises(TypeError, area_of_circle, 5+3j)
        self.assertRaises(TypeError, area_of_circle, "radius")
        self.assertRaises(TypeError, area_of_circle, True)


