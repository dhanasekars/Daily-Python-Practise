""" 
Created on : 29/01/23 4:50 AM
@author : ds  
"""

import unittest
from Jan_29 import sorting_list

class TestSortingList(unittest.TestCase):
    def test_sorting_list(self):
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        self.assertEqual(sorting_list([]), [])
        self.assertEqual(sorting_list([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, "15"]), "List contains non-numeric values.")
