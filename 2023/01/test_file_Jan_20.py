""" 
Created on : 20/01/23 4:33 AM
@author : ds  
"""

import unittest
from Jan_20 import gradingStudents


class TestGradingStudents(unittest.TestCase):

    def test_grading_students(self):
        self.assertEqual(gradingStudents([73, 67, 38, 33]), [75, 67, 40, 33])
        self.assertEqual(gradingStudents([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 40, 40])