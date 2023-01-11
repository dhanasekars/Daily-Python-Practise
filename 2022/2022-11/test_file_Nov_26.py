""" 
Created on : 26/11/22 4:43 AM
@author : ds  
"""

import unittest
from Nov_26 import Name


class testName(unittest.TestCase):

    def test_fullname(self):
        n1 = Name("hello", "world")
        self.assertEqual(n1.fullname, "Hello World")
        n2 = Name("Dhana", "s")
        self.assertEqual(n2.fullname, "Dhana S")

    def test_fname(self):
        n1 = Name("HELLO", "world")
        self.assertEqual(n1.fname, "Hello")
        n2 = Name("Dhana", "s")
        self.assertEqual(n2.fname, "Dhana")

    def test_lname(self):
        n1 = Name("HeLLO", "WORlD")
        self.assertEqual(n1.lname, "World")
        n2 = Name("Dhana", "s")
        self.assertEqual(n2.lname, "S")

    def test_initials(self):
        n1 = Name("Hello", "Python")
        self.assertEqual(n1.initials, "H.P")
        n2 = Name("Dhana", "s")
        self.assertEqual(n2.initials, "D.S")