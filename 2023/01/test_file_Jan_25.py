""" 
Created on : 25/01/23 4:41 AM
@author : ds  
"""

import unittest
from Jan_25 import exercise_1

class TestExercise1(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(exercise_1([]), "Empty list")

    def test_non_numeric_list(self):
        self.assertEqual(exercise_1(['a', 'b', 'c']), "List contains non-numeric values.")

    def test_numeric_list(self):
        self.assertEqual(exercise_1([1, 2, 3, 4, 5]), 4)
        self.assertEqual(exercise_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 9)
        self.assertEqual(exercise_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 14)
        self.assertEqual(exercise_1([1, 1]), 0)


