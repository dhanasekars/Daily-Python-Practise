""" 
Created on : 31/01/23 4:50 AM
@author : ds  
"""

import unittest
from Jan_31 import stringcap, common_char

class TestJan31(unittest.TestCase):
    def testupper(self):
        self.assertTrue(stringcap("HellO"))
        self.assertFalse(stringcap("hello"))
        self.assertFalse(stringcap("hello world"))
        self.assertFalse(stringcap("hello world!"))
        self.assertEqual(stringcap(""), "Empty String")
        self.assertEqual(stringcap(1), "List contains non-numeric values.")

    def testcommonchar(self):
        self.assertEqual(common_char("phone", "home"), {'e', 'h', 'o'})
        self.assertEqual(common_char("abc", "def"), set())