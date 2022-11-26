""" 
Created on : 26/11/22 3:22 PM
@author : ds  
"""

from Nov_25 import Student, Testpaper
import unittest

class test_Testpaper(unittest.TestCase):

    def test_subject(self):
        paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
        self.assertEqual(paper1.subject, "Maths")

    def test_markscheme(self):
        paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
        self.assertEqual(paper1.markscheme, ["1A", "2C", "3D", "4A", "5A"])

    def test_pass_mark(self):
        paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
        self.assertEqual(paper1.pass_mark, "60%")

    def test_no_tests_taken(self):
        student1 = Student()
        self.assertEqual(student1.tests_taken, "No tests taken")

    def test_student_tests_taken(self):
        paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
        paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
        paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
        student1 = Student()
        student2 = Student()
        self.assertEqual(student1.tests_taken, "No tests taken")
        student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
        self.assertEqual(student1.tests_taken, {"Maths": "Passed! (80%)"})
        student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
        student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
        self.assertEqual(student2.tests_taken, {"Chemistry": "Failed! (25%)", "Computing": "Failed! (42%)"})
