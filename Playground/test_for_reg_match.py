""" 
Created on : 03 AutomateBoringStuffs/02/23 1:20 PM
@author : ds  
"""
import unittest, re
from regexexercise import count_match


class testRegEx(unittest.TestCase):
    def testCount(self):
        self.assertEqual(count_match("horse", "horse"), 1)
        self.assertEqual(count_match("horseinthebarnmanonthehorsehorseofranch", "horse"), 3)
        self.assertEqual(count_match("horse", "CAMEL"), 0)

