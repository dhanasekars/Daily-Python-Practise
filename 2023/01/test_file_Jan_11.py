""" 
Created on : 11/01/23 9:37 AM
@author : ds  
"""
import unittest
from Jan_11 import plusMinus


class test_plusMinus(unittest.TestCase):
    def test_plusMinus(self):
        self.assertEqual(plusMinus([1, 1, 0, -1, -1]), ['0.400000', '0.400000', '0.200000'])
        self.assertEqual(plusMinus([1, 2, 3, -1, -2, -3, 0, 0]), ['0.375000', '0.375000', '0.250000'])
        self.assertEqual(plusMinus([-4, 3, -9, 0, 4, 1]), ['0.500000', '0.333333', '0.166667'])