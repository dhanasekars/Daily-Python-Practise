""" 
Created on : 26/01/23 5:26 AM
@author : ds  
"""

import unittest
from Jan_26 import largestsumlist

class TestLargestSumList(unittest.TestCase):
    def testSumList(self):
        self.assertEqual(largestsumlist([1, 2, 3], [4, 5, 6], [10, 11, 12]), [10, 11, 12])
        self.assertEqual(largestsumlist([1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]), [10, 11, 12])
        self.assertEqual(largestsumlist([1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15]), [13, 14, 15])
        self.assertEqual(largestsumlist([1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15], [16, 17, 18]), [16, 17, 18])
        self.assertEqual(largestsumlist([1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9], [13, 14, 15], [16, 17, 18], [19, 20, 21]), [19, 20, 21])