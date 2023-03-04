""" 
Created on : 13/01/23 11:03 AutomateBoringStuffs AM
@author : ds  
"""
import unittest
from Jan_13 import miniMaxSum

class test_miniMaxSum(unittest.TestCase):

    def test_minmax(self):
        self.assertEqual(miniMaxSum([1, 2, 3, 4, 5]), [10, 14])
        self.assertEqual(miniMaxSum([7, 69, 2, 221, 8974]), [299, 9271])
        self.assertEqual(miniMaxSum([1, 3, 5, 7, 9]), [16, 24])
        self.assertEqual(miniMaxSum([1, 2, 3, 4, 5]), [10, 14])
        self.assertEqual(miniMaxSum([7, 69, 2, 221, 8974]), [299, 9271])
        self.assertEqual(miniMaxSum([1, 3, 5, 7, 9]), [16, 24])
        self.assertEqual(miniMaxSum([0, 0, 0, 1, 0]), [0, 1])