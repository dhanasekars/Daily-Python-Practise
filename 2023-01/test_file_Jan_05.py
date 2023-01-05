""" 
Created on : 05/01/23 11:26 AM
@author : ds  
"""
import unittest

from Jan_05 import EvenStream, OddStream, print_from_stream


class TestStream(unittest.TestCase):

    def test_odd_stream(self):
        self.assertEqual(print_from_stream(2, OddStream()), (1, 3))
