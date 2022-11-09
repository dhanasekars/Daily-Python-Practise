""" 
Created on : 07/11/22 6:00 AM
@author : ds  
"""

import unittest
from Nov_09_Set import same_vowel_group


class TestSameVowel(unittest.TestCase):
    def test_two(self):
        self.assertEqual(["toe", "ocelot"], same_vowel_group(["toe", "ocelot", "maniac"]))

    def test_one(self):
        self.assertEqual(['many'], same_vowel_group(["carriage", "emit", "apricot", "animal"]))

    def test_three(self):
        self.assertEqual(["hoops", "bot", "bottom"], same_vowel_group(["hoops", "chuff", "bot", "bottom"]))