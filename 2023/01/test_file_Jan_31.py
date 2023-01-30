""" 
Created on : 31/01/23 4:50 AM
@author : ds  
"""

import unittest
from Jan_31 import stringcap

class TestJan31(unittest.TestCase):
    def testupper(self):
        self.assertTrue(stringcap("HellO"))
        self.assertFalse(stringcap("hello"))
        self.assertFalse(stringcap("hello world"))
        self.assertFalse(stringcap("hello world!"))
        self.assertEqual(stringcap(""), "Empty String")
        self.assertEqual(stringcap(1), "List contains non-numeric values.")
