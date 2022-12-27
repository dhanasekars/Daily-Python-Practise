""" 
Created on : 27/12/22 5:28 AM
@author : ds  
"""

from Dec_27 import list_of_multiples,add
import unittest

class TestMultiples(unittest.TestCase):

    def test_multiples(self):
        self.assertEqual(list_of_multiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
        self.assertEqual(list_of_multiples(17, 7), [17, 34, 51, 68, 85, 102, 119])
        self.assertEqual(list_of_multiples(630, 14),
                           [630, 1260, 1890, 2520, 3150, 3780, 4410, 5040, 5670, 6300, 6930, 7560, 8190, 8820])
        self.assertEqual(list_of_multiples(140, 3), [140, 280, 420])
        self.assertEqual(list_of_multiples(7, 8), [7, 14, 21, 28, 35, 42, 49, 56])
        self.assertEqual(list_of_multiples(11, 21),
                           [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165, 176, 187, 198, 209, 220,
                            231])

    def test_add(self):
        self.assertEqual(add("2", "3"), "5")
        self.assertEqual(add("91", "19"), "110")
        self.assertEqual(add("123456789", "987654322"), "1111111111")
        self.assertEqual(add("9999999", "1"), "10000000")
        self.assertEqual(add("300", "3000"), "3300")
        self.assertEqual(add("1000", "6200"), "7200")
        self.assertEqual(add("-10", "-20"), "-30")
        self.assertEqual(add("-100", "100"), "0")
        self.assertEqual(add("0", "6200"), "6200")
        self.assertEqual(add("", "6"), "Invalid Operation")
        self.assertEqual(add("", None), "Invalid Operation")
        self.assertEqual(add(None, "23"), "Invalid Operation")
        self.assertEqual(add("", "20"), "Invalid Operation")