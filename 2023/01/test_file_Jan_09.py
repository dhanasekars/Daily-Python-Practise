""" 
Created on : 09/01/23 9:33 AM
@author : ds  
"""
import unittest
from Jan_09 import aVeryBigSum

class testAVeryBigSum(unittest.TestCase):
    def test_aVeryBigSum(self):
        self.assertEqual(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]), 5000000015)