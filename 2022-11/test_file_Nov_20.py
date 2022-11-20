""" 
Created on : 20/11/22 5:52 AM
@author : ds  
"""

import unittest
from Nov_20 import Pagination


class TestPagination(unittest.TestCase):

    def test_totalPages(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = Pagination(alphabetList, 5)
        self.assertEqual(p1.getTotalPages(), 5)
        p2 = Pagination(alphabetList, 6)
        self.assertEqual(p2.getTotalPages(), 5)
        p3 = Pagination(alphabetList, 7)
        self.assertEqual(p3.getTotalPages(), 4)

    def test_goToPage(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = Pagination(alphabetList, 5)
        self.assertEqual(p1.goToPage(1), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(p1.goToPage(5), ['y'])
        self.assertEqual(p1.goToPage(10), ['y'])
        self.assertEqual(p1.goToPage(-5), ['a', 'b', 'c', 'd', 'e'])




