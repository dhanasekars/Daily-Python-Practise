""" 
Created on : 11/11/22 5:41 AM
@author : ds  
"""
import unittest
from Nov_11 import multiplication_table


class TestMultiplicationTable(unittest.TestCase):

    def test_one(self):
        self.assertEqual([[1]], multiplication_table(1))

    def test_three(self):
        self.assertEqual([[1, 2, 3], [2, 4, 6], [3, 6, 9]], multiplication_table(3))

    def test_five(self):
        self.assertEqual([[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
, multiplication_table(5))
