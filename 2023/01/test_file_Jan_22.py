""" 
Created on : 22/01/23 4:51 AM
@author : ds  
"""

import unittest
from Jan_22 import breakingRecords

class TestBreakingRecords(unittest.TestCase):
    def test_breakingRecords(self):
        self.assertEqual(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4])
        self.assertEqual(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])
        self.assertEqual(breakingRecords([0, 9, 3, 10, 2, 20]), [3, 0])