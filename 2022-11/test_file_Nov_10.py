""" 
Created on : 10/11/22 5:54 AM
@author : ds  
"""

import unittest
from Nov_10_class import player


class TestClass(unittest.TestCase):

    def test_age(self):
        p1 = player("David Jones", 25, 175, 75)
        p2 = player(" ", 0, 175, 75)
        self.assertEqual("David Jones is age 25", p1.get_age())
        self.assertEqual("  is age 0", p2.get_age())

    def test_height(self):
        p1 = player("Malar Teacher", 25, 175, 75)
        p2 = player(" ", 25, 0, 75)
        self.assertEqual("Malar Teacher is 175cm", p1.get_height())
        self.assertEqual("  is 0cm", p2.get_height())

    def test_weight(self):
        p1 = player("Kajol", 25, 175, 75)
        p2 = player(" ", 25, 0, 75)
        self.assertEqual("Kajol weights 75kg", p1.get_weight())
        self.assertEqual("  is 0kg", p2.get_weight())