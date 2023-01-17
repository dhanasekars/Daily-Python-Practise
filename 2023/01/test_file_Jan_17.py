""" 
Created on : 17/01/23 5:55 AM
@author : ds  
"""

import unittest
from Jan_17 import formingMagicSquare


class TestFormingMagicSquare(unittest.TestCase):
    def testMagicSquare(self):
        s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
        self.assertEqual(formingMagicSquare(s), 1)
        s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
        self.assertEqual(formingMagicSquare(s), 4)
        s = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]
        self.assertEqual(formingMagicSquare(s), 14)