""" 
Created on : 13/08/23 11:13 am
@author : ds  
"""

import unittest

def calculate(num=100):
    # numbers = []
    # for i in range(num):
    #     if i % 5 == 0 or i % 7 == 0:
    #         numbers.append(i)
    return sum([i for i in range(num) if i % 5 == 0 or i % 7 == 0 ])


class Test_Sum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(calculate(0), 0)

    def test_Hundred(self):
        self.assertEqual(calculate(), 1580)
