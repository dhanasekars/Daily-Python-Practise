""" 
Created on : 07/11/22 5:36 AM
@author : ds  
"""

import unittest
from Nov_07_is_instance import num_of_sublists


class TestSublist(unittest.TestCase):

    def test_single_list(self):
        self.assertEqual(1, num_of_sublists([[1, 2, 3]]))

    def test_zero_list(self):
        self.assertEqual(1, num_of_sublists([1, 2, 3]))

    def test_zero_Len_list(self):
        self.assertEqual(1, num_of_sublists([]))

    def test_more_lists(self):
        self.assertEqual(4, num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]))