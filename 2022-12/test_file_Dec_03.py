""" 
Created on : 03/12/22 4:41 AM
@author : ds  
"""

import unittest
from Dec_03_Four_Vectors import FourVectorOperators

class test_VectorOperators(unittest.TestCase):

    def test_addition(self):
        v0 = FourVectorOperators([0, 0, 0, 0])
        v1 = FourVectorOperators([1, 2, 3, -4])
        v2 = FourVectorOperators([1, 0, 0, 1])
        self.assertEqual(v0 + v1, FourVectorOperators([1, 2, 3, -4]))
        self.assertEqual(v1 + v2, FourVectorOperators([2, 2, 3, -3]))

    def test_subtraction(self):
        v0 = FourVectorOperators([0, 0, 0, 0])
        v1 = FourVectorOperators([1, 2, 3, -4])
        v2 = FourVectorOperators([1, 0, 0, 1])
        self.assertEqual(v0 - v1, FourVectorOperators([-1, -2, -3, 4]))
        self.assertEqual(v1 - v2, FourVectorOperators([0, 2, 3, -5]))

    def test_equal(self):
        v0 = FourVectorOperators([0, 0, 0, 0])
        v1 = FourVectorOperators([1, 2, 3, -4])
        v2 = FourVectorOperators([1, 0, 0, 1])
        v3 = FourVectorOperators([1, 2, 3, -4])
        v4 = FourVectorOperators([2, 2, 3, -3])

        self.assertEqual(v0 == v1, False)
        self.assertEqual(v1 == v3, True)
        self.assertEqual((v1 + v2) == v4, True)
        self.assertEqual((v1 + v2) == v3, False)

