""" 
Created on : 16/11/22 6:12 AM
@author : ds  
"""
import unittest

from Nov_17 import Circle
from math import pi


class TestCircle(unittest.TestCase):

    def test_zero(self):
        c0 = Circle()
        self.assertEqual(0, c0.getArea())
        self.assertEqual(0, c0.getPerimeter())

    def test_fraction(self):
        c0 = Circle(0.5)
        self.assertAlmostEqual(c0.getArea(), 0.78539816)
        self.assertAlmostEqual(c0.getPerimeter(), 3.14159265)