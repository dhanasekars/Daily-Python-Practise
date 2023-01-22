""" 
Created on : 23/01/23 4:51 AM
@author : ds  
"""

import unittest
from Jan_23_leap_year import dayOfProgrammer

class TestDayofProgrammer(unittest.TestCase):

    def test_day_of_programmer(self):
        self.assertEqual(dayOfProgrammer(2017), '13.09.2017')
        self.assertEqual(dayOfProgrammer(2016), '12.09.2016')
        self.assertEqual(dayOfProgrammer(1800), '12.09.1800')
        self.assertEqual(dayOfProgrammer(1918), '26.09.1918')
        self.assertEqual(dayOfProgrammer(1917), '13.09.1917')
        self.assertEqual(dayOfProgrammer(1916), '12.09.1916')




