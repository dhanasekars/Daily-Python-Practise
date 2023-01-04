""" 
Created on : 04/01/23 3:14 PM
@author : ds  
"""
import unittest

from Jan_04_Debug import is_vowel, score_words


class testScore(unittest.TestCase):

    def test_zero_score(self):
        self.assertEqual(score_words(["wdfg", "fghj", "zxcvbnm"]), 0)

    def test_odd_vowel_score(self):
        self.assertEqual(score_words(["hack"]), 1)
        self.assertEqual(score_words(["hack", "is"]), 2)

    def test_even_vowel_score(self):
        self.assertEqual(score_words(["hacker", "book"]), 4)
        self.assertEqual(score_words(["beer", "whisky", "vodka"]), 6)

    def test_mixed_score(self):
        self.assertEqual(score_words(["hack", "book"]), 3)
        self.assertEqual(score_words(["beer", "whiskey", "vodka"]), 5)

