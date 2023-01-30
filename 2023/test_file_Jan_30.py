""" 
Created on : 30/01/23 9:35 AM
@author : ds  
"""
import unittest
from Jan_30 import odd_even_difference

class TestJan30(unittest.TestCase):
    def test_odd_even_difference(self):
        self.assertEqual(odd_even_difference([1, 3, 5, 9, 18, 4]), 4)
        self.assertEqual(odd_even_difference([1, 2, 99, 4, 8, 10, 13]), 89)
        self.assertEqual(odd_even_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 8)
        self.assertEqual(odd_even_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), 9)
        self.assertEqual(odd_even_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 10)
        self.assertEqual(odd_even_difference([]), 0)
        self.assertEqual(odd_even_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "20"]), "List contains non-numeric values.")
