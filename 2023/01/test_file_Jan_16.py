""" 
Created on : 16/01/23 8:51 AM
@author : ds  
"""

import unittest
from Jan_16 import birthdayCakeCandles


class TestBirthdayCandles(unittest.TestCase):

    def test_birthdayCakeCandles(self):
        self.assertEqual(birthdayCakeCandles([3, 2, 1, 3]), 2)
        self.assertEqual(birthdayCakeCandles([4, 4, 1, 3]), 2)
        self.assertEqual(birthdayCakeCandles([82, 49, 82, 82, 41, 82, 15, 63, 38, 25]), 4)
        self.assertEqual(birthdayCakeCandles([18, 90, 90, 13, 90, 75, 90, 8, 90, 43]), 5)
        self.assertEqual(birthdayCakeCandles([44, 53, 31, 27, 77, 60, 66, 77, 26, 36]), 2)
        self.assertEqual(birthdayCakeCandles([1, 2, 3]), 1)
        self.assertEqual(birthdayCakeCandles([0, 0, 0]), 3)
