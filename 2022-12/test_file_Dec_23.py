""" 
Created on : 23/12/22 6:16 AM
@author : ds  
"""
import unittest

from Dec_23 import equilibrium, not_share

class TestDec23(unittest.TestCase):

    def test_equilibrium(self):
        self.assertEqual(equilibrium(0), True)
        self.assertEqual(equilibrium(0.2), "positive")
        self.assertEqual(equilibrium(-1), "negative")

    def test_not_share(self):
        self.assertEqual(not_share([1, 2, 3], [4, 5, 6]), True)
        self.assertEqual(not_share([1, 2, 3, 4, 5, 6], [6]), False)
        self.assertEqual(not_share([1], [2, 3, 4, 5, 6, 7]), True)
        self.assertEqual(not_share([3, 3, 3], [1, 2, 3]), False)
        self.assertEqual(not_share([1], [1, 2, 3, 4, 5, 6]), False)
