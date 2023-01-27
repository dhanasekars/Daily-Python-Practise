""" 
Created on : 28/01/23 5:12 AM
@author : ds  
"""
import unittest
from Jan_28 import product_of_large_number

class TestJan28(unittest.TestCase):
    def test_product_of_large_number(self):
        self.assertEqual(product_of_large_number([1, 2, 3], [4, 5, 6], [7, 8, 9]), 162)
        self.assertEqual(product_of_large_number([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]), 29160)
        self.assertEqual(product_of_large_number([1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]), 1458)
        self.assertEqual(product_of_large_number([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]), 1944)
        self.assertEqual(product_of_large_number([]), "Empty list")
        self.assertEqual(product_of_large_number([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, "15"]), "List contains non-numeric values.")