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

    def test_createPages(self):
        alphabetList = list("abcdefghijklmnopqrstuvwxy")
        p1 = Pagination(alphabetList, 25)
        self.assertEqual(p1.createPages(), [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']])
        alphabetList = list("abcde")
        p2 = Pagination(alphabetList, 1)
        self.assertEqual(p2.createPages(), [['a'], ['b'], ['c'], ['d'], ['e']]
)