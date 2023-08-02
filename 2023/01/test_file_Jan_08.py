""" 
Created on : 08 graphQL/01/23 2:52 PM
@author : ds  
"""
import unittest
from Jan_08 import compareTriplets

class testCompareTriplets(unittest.TestCase):
    def test_compareTriplets(self):
        self.assertEqual(compareTriplets([5, 6, 7], [3, 6, 10]), (1, 1))
        self.assertEqual(compareTriplets([17, 28, 30], [99, 16, 8]), (2, 1))