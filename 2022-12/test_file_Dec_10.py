""" 
Created on : 10/12/22 5:15 AM
@author : ds  
"""
import unittest
from Dec_10 import FourVectors2


class TestFourVectors2(unittest.TestCase):

    def test_initialization(self):
        four_vectors = FourVectors2()
        self.assertEqual(four_vectors.components, [0.0, 0.0, 0.0, 0.0])

    def test_multiply_two_vectors(self):
        v1 = FourVectors2([1, 2, 3, 4])
        v2 = FourVectors2([1, 0, 0, 1])
        self.assertEqual(v1*v2, -3)

    def test_get_Length(self):
        v3 = FourVectors2([1, 0, 1, 0])
        v4 = FourVectors2([-1, 4, 1, 2])
        v5 = FourVectors2([-1, 37, 55, -108])
        v6 = FourVectors2([0.5, 1.0, -2.0, 10.0])
        self.assertAlmostEqual(FourVectors2.GetLength(v6), 10.23474474)
        self.assertAlmostEqual(FourVectors2.GetLength(v3), 0)