""" 
Created on : 21/12/22 5:08 AM
@author : ds  
"""

from Dec_21_MinimalClass import Minimal
import unittest

class TestMinimal(unittest.TestCase):

    def test_minimal_if(self):
        minimal = Minimal()
        self.assertEqual(minimal.minimal_if(6), True)
        self.assertEqual(minimal.minimal_if(1), False)

    def test_boolean_redundancy(self):
        minimal = Minimal()
        self.assertEqual(minimal.boolean_redundancy(6), 'even')
        self.assertEqual(minimal.boolean_redundancy(3), 'odd')