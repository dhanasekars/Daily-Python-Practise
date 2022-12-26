""" 
Created on : 26/12/22 5:41 AM
@author : ds
https://edabit.com/challenge/8vBvgJMc2uQJpD6d7
"""

from Dec_26 import prime_factors
import unittest

class TestPrimeFactors(unittest.TestCase):

    def test_prime(self):
        self.assertEqual(prime_factors(20), [2, 2, 5])
        self.assertEqual(prime_factors(100), [2, 2, 5, 5])
        self.assertEqual(prime_factors(8912234), [2, 47, 94811])