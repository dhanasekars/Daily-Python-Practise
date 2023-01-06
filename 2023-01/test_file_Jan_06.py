""" 
Created on : 06/01/23 10:12 AM
@author : ds
"""
import unittest

from Jan_06 import mutate_string

class TestMutate(unittest.TestCase):

    def test_one_character(self):
        self.assertEqual(mutate_string("d", 0, "k"), "k")

    def test_multiple_character(self):
        self.assertEqual(mutate_string("test", 0, "b"), "best")
        self.assertEqual(mutate_string("peat", 3, "k"), "peak")

    def test_index_error_character(self):
        self.assertEqual(mutate_string("", 0, "b"), "Position provided is invalid!")
        self.assertEqual(mutate_string("peat", 6, "k"), "Position provided is invalid!")

