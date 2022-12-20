""" 
Created on : 20/12/22 5:43 AM
@author : ds  
"""

from Dec_20 import CleanUp
import unittest

class TestCleanUp(unittest.TestCase):

    def test_clean_up(self):
        cleanup = CleanUp([38, 80, 13, 73, 66, 70, 83, 6, 93, 9, 7, 8, 41])
        self.assertEqual(cleanup.clean_up_list(), [[38, 80, 66, 70, 6, 8],[13, 73, 83, 93, 9, 7, 41]])
        cleanup = CleanUp([38, 80])
        self.assertEqual(cleanup.clean_up_list(), [[38, 80], []])
        cleanup = CleanUp([39, 81])
        self.assertEqual(cleanup.clean_up_list(), [[], [39, 81]])
