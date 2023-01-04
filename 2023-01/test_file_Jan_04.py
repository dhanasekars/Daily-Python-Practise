""" 
Created on : 04/01/23 3:14 PM
@author : ds  
"""
import unittest

from Jan_04_Debug import is_vowel, score_words


class testScore(unittest.TestCase):

    def test_two_words(self):
        self.assertEqual(score_words(["hacker", "book"]), 4)

    def test_three_words(self):
        self.assertEqual(score_words(["wdfg", "fghj", "zxcvbnm"]), 0)
