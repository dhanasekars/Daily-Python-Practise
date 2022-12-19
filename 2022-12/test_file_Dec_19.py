""" 
Created on : 19/12/22 1:19 PM
@author : ds  
"""

from Dec_19 import Taxi
import unittest

class TestTaxi(unittest.TestCase):

    def test_distance(self):
        taxi = Taxi(3)
        self.assertEqual(taxi.calc_distance(), 1)
        taxi = Taxi(5)
        self.assertEqual(taxi.calc_distance(), 2)
        taxi = Taxi(0)
        self.assertEqual(taxi.calc_distance(), 0)
        taxi = Taxi(11037)
        self.assertEqual(taxi.calc_distance(), 5518)

