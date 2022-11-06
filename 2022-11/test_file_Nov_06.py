""" 
Created on : 06/11/22 5:34 AM
@author : ds  
"""
import unittest
from Nov_06 import split


class TestSplit(unittest.TestCase):
    def test_split(self):
        # test the parenthesis for valid inputs
        self.assertEqual(split("()()()"), ["()", "()", "()"])

    def test_split1(self):
        # test the parenthesis for valid inputs
        self.assertEqual(split("((()))(())()()(()())"), ["((()))", "(())", "()", "()", "(()())"])

    def test_split2(self):
        # test for one set of parenthesis
        self.assertEqual(split("((()))"), ["((()))"])

    def test_split3(self):
        # test for one set of parenthesis
        self.assertEqual(split("((())())(()(()()))"), ["((())())", "(()(()()))"])

    def test_split_empty(self):
        self.assertEqual(split(""), [])
