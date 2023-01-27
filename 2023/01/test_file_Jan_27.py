""" 
Created on : 27/01/23 4:44 AM
@author : ds  
"""
import unittest
from Jan_27 import single_largest_value, max_values_list, max_position_list

class TestJan27(unittest.TestCase):
    def test_single_largest_value(self):
        self.assertEqual(single_largest_value([1, 2, 3], [4, 5, 6], [7, 8, 9]), [7, 8, 9])
        self.assertEqual(single_largest_value([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]), [10, 11, 12])
        self.assertEqual(single_largest_value([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]), [13, 14, 15])
        self.assertEqual(single_largest_value([1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]), [7, 8, 9])
        self.assertEqual(single_largest_value([]), "Empty list")
        self.assertEqual(single_largest_value([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, "15"]), "List contains non-numeric values.")

    def test_max_values_from_list(self):
        self.assertEqual(max_values_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [9, 6, 3])
        self.assertEqual(max_values_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]), [15, 12, 9, 6, 3])
        self.assertEqual(max_values_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]), [9, 9, 6, 3])
        self.assertEqual(max_values_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]), [12, 9, 6, 3])
        self.assertEqual(max_values_list([]), "Empty list")
        self.assertEqual(max_values_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, "15"]), "List contains non-numeric values.")

    def test_max_position_list(self):
        self.assertEqual(max_position_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [7, 8, 9])
        self.assertEqual(max_position_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]), [13, 14, 15])
        self.assertEqual(max_position_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]), [7, 8, 9])
        self.assertEqual(max_position_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]), [10, 11, 12])
        # self.assertEqual(max_position_list([]), "Empty list")
        self.assertEqual(max_position_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, "15"]), "List contains non-numeric values.")
