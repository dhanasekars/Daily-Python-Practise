""" 
Created on : 24/01/23 8:58 AM
@author : ds  
"""

import unittest
from Jan_24 import catAndMouse

class TestCatAndMouse(unittest.TestCase):
    def test_cat_and_mouse(self):
        self.assertEqual(catAndMouse(1, 2, 3), 'Cat B')
        self.assertEqual(catAndMouse(1, 3, 2), 'Mouse C')
        self.assertEqual(catAndMouse(2, 1, 3), 'Cat A')
        self.assertEqual(catAndMouse(1, 3, 2), 'Mouse C')
        self.assertEqual(catAndMouse(1, 2, 3), 'Cat B')