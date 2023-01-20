""" 
Created on : 21/01/23 4:57 AM
@author : ds  
"""

import unittest
from Jan_21 import kangaroo

class TestKangaroo(unittest.TestCase):
    def test_kangaroo(self):
        self.assertEqual(kangaroo(0, 3, 4, 2), 'YES')
        self.assertEqual(kangaroo(0, 2, 5, 3), 'NO')
        self.assertEqual(kangaroo(0, 2, 1, 2), 'NO')