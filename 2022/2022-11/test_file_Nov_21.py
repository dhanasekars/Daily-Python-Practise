""" 
Created on : 20/11/22 5:52 AM
@author : ds  
"""

import unittest
from Nov_21_inheritance import ExtendPagination


class TestExtendPagination(unittest.TestCase):

    def test_goToPage(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = ExtendPagination(alphabetList, 5)
        self.assertEqual(p1.goToPage(1), 1)
        self.assertEqual(p1.goToPage(3), 3)
        self.assertEqual(p1.goToPage(5), 5)
        self.assertEqual(p1.goToPage(-7), 1)
        self.assertEqual(p1.goToPage(6), 5)

    def test_getVisibleItems(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxyz")
        p1 = ExtendPagination(alphabetList, 4)
        self.assertEqual(p1.getVisibleItems(), ['a', 'b', 'c', 'd'])
        alphabetList = list("a")
        p1 = ExtendPagination(alphabetList, 25)
        self.assertEqual(p1.getVisibleItems(), ['a'])

