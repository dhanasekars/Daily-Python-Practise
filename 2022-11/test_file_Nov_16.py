""" 
Created on : 16/11/22 5:46 AM
@author : ds  
"""

import unittest
from Nov_16 import Calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(7, calculator.add(1, 6))
        self.assertEqual(6, calculator.add(0, 6))
        self.assertEqual(6, calculator.add(6, 0))
        self.assertEqual(0, calculator.add(1, -1))

    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(-7, calculator.subtract(1, 8))
        self.assertEqual(-6, calculator.subtract(0, 6))
        self.assertEqual(6, calculator.subtract(6, 0))
        self.assertEqual(2, calculator.subtract(1, -1))

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(8, calculator.multiply(1, 8))
        self.assertEqual(0, calculator.multiply(0, 6))
        self.assertEqual(0, calculator.multiply(6, 0))
        self.assertEqual(-1, calculator.multiply(1, -1))

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(0.125, calculator.divide(1, 8))
        self.assertEqual(0, calculator.divide(0, 6))
        self.assertEqual(1, calculator.divide(6, 6))
        self.assertEqual(-1, calculator.divide(1, -1))
