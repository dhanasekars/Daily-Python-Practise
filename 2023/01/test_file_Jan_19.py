""" 
Created on : 19/01/23 5:24 AM
@author : ds  
"""
import unittest
from Jan_19 import timeConversion


class TestTimeConversion(unittest.TestCase):
    def testTimeConversion(self):
        s = "07:05:45PM"
        self.assertEqual(timeConversion(s), "19:05:45")
        s = "12:40:22AM"
        self.assertEqual(timeConversion(s), "00:40:22")
        s = "12:45:54PM"
        self.assertEqual(timeConversion(s), "12:45:54")
        s = "00:00:00AM"
        self.assertEqual(timeConversion(s), "00:00:00")
        s = "12:00:00PM"
        self.assertEqual(timeConversion(s), "12:00:00")
        s = "01:00:00PM"
        self.assertEqual(timeConversion(s), "13:00:00")