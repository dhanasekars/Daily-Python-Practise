""" 
Created on : 02/12/22 4:55 AM
@author : ds  
"""

import unittest
from Dec_02 import FourVector


class testFourVector(unittest.TestCase):

    def test_GetComponents(self):
        v0 = FourVector()
        v1 = FourVector([0, 0, 0, 0])
        v2 = FourVector([1, 2, 3, 4])
        self.assertEqual(v0.GetComponents(), [0, 0, 0, 0])
        self.assertEqual(v1.GetComponents(), [0, 0, 0, 0])
        self.assertEqual(v2.GetComponents(), [1, 2, 3, 4])

    def test_SetComponents(self):
        v2 = FourVector()
        v3 = FourVector()
        v2.SetComponents([1, 0, 0, 1])
        self.assertEqual(v2.GetComponents(), [1, 0, 0, 1])
        v3.SetComponents([-1, 0, 1, 0])
        self.assertEqual(v3.GetComponents(), [-1, 0, 1, 0])

    def test_str(self):
        v0 = FourVector()
        v1 = FourVector([0, 0, 0, 0])
        v2 = FourVector([1, -2.3, 3.5, 4])
        self.assertEqual(str(v0), "(0.0, 0.0, 0.0, 0.0)")
        self.assertEqual(str(v1), "(0, 0, 0, 0)")
        self.assertEqual(str(v2), "(1, -2.3, 3.5, 4)")

    # def test_add(self):
    #     v0 = FourVector([0, 0, 0, 0])
    #     v1 = FourVector([1, 2, 3, 4])
    #     self.assertEqual(v0 + v1,[1, 2, 3, 4])