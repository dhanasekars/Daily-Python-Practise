""" 
Created on : 10/01/23 9:37 AM
@author : ds  
"""

import unittest
from Jan_10 import diagonalDifference

class test_diagonalDifference(unittest.TestCase):
    def test_diagonalDifference(self):
        self.assertEqual(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)
        self.assertEqual(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]), 2)
        self.assertEqual(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]), 2)
        self.assertEqual(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]), 2)


