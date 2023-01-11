""" 
Created on : 22/11/22 5:54 AM
@author : ds  
"""

import unittest
from Nov_22_double_inheritance import PageNavigation


class TestPageNavigation(unittest.TestCase):

    def test_goToFirstPage(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = PageNavigation(alphabetList, 5)
        self.assertEqual(p1.goToFirstPage(), 1)
        p1.goToPage(4)
        self.assertEqual(p1.goToFirstPage(), 1)

    def test_goToLastPage(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = PageNavigation(alphabetList, 5)
        self.assertEqual(p1.goToLastPage(), 5)
        p1.goToPage(3)
        self.assertEqual(p1.goToLastPage(), 5)