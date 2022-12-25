""" 
Created on : 25/12/22 5:43 AM
@author : ds  
"""

from Dec_25 import find_highest
import unittest

class TestHighest(unittest.TestCase):

    def test_highest(self):
        self.assertEqual(find_highest([8]), 8)
        self.assertEqual(find_highest([-1, 3, 5, 6, 99, 12, 2]), 99)
        self.assertEqual(find_highest([0, 12, 4, 87]), 87)