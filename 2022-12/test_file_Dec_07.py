""" 
Created on : 07/12/22 4:50 AM
@author : ds  
"""

from Dec_07 import Person
import unittest

class testPerson(unittest.TestCase):

    def test_initiation(self):
        p1 = Person("Sam", ["ice cream"], ["carrots"])
        self.assertEqual(p1.name, "Sam")
        self.assertEqual(p1.likes, ["ice cream"])
        self.assertEqual(p1.dislikes, ["carrots"])

    def test_taste(self):
        p1 = Person("Sam", ["ice cream"], ["carrots"])
        self.assertEqual(p1.taste("ice cream"), "Sam eats the ice cream and loves it!")
        self.assertEqual(p1.taste("carrots"), "Sam eats the carrots and hates it!")
        self.assertEqual(p1.taste("whisky"), "Sam eats the whisky!")
