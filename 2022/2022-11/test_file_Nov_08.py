""" 
Created on : 07/11/22 6:00 AM
@author : ds  
"""

import unittest
from Nov_08_lambda import num_type


class TestNumtype(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual('Perfect', num_type(6))

    def test_amicable(self):
        self.assertEqual('Amicable', num_type(2924))

    def test_neither(self):
        self.assertEqual('Neither', num_type(5010))