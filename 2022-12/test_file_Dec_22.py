""" 
Created on : 22/12/22 5:35 AM
@author : ds  
"""
import unittest

from Dec_22 import is_prime


class TestPrime(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(104729), True)