""" 
Created on : 07/01/23 6:03 AutomateBoringStuffs PM
@author : ds
https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
"""
import unittest

from Jan_07 import simpleArraySum

class test_simpleArraySum(unittest.TestCase):

    def test_simpleArraySum(self):
        self.assertEqual(simpleArraySum([1, 2, 3, 4, 10, 11]), 31)
        self.assertEqual(simpleArraySum([0]), 0)