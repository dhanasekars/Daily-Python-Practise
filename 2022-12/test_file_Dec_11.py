""" 
Created on : 11/12/22 5:30 AM
@author : ds  
"""

import unittest
from Dec_11 import Lever


class TestLever(unittest.TestCase):

    def test_setlever(self):
        lever = Lever()
        lever.SetLever(["e", "f", "l"])
        self.assertEqual(lever.lever, ["e", "f", "l"])

    def test_getlever(self):
        lever = Lever()
        lever.SetLever(["e", "f", "l"])
        self.assertEqual(lever.GetLever(), ["e", "f", "l"])

    def test_determine_lever(self):
        lever1 = Lever()
        lever1.SetLever(["e", "f", "l"])
        self.assertEqual(lever1.determine_lever(), "first class lever")
        lever1.SetLever(["e", "l", "f"])
        self.assertEqual(lever1.determine_lever(), "second class lever")
        lever1.SetLever(["f", "e", "l"])
        self.assertEqual(lever1.determine_lever(), "third class lever")
