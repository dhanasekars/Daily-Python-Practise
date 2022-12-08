""" 
Created on : 08/12/22 5:35 AM
@author : ds  
"""

from Dec_08 import AvoidExec
import unittest


class TestAvoidExec(unittest.TestCase):

    def test_search(self):
        self.assertEqual(AvoidExec(), AvoidExec().res == AvoidExec().users)
