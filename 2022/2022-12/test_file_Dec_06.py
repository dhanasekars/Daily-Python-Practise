""" 
Created on : 06/12/22 4:33 AM
@author : ds  
"""

from Dec_06_representing_millions import Country
import unittest


class TestCountry(unittest.TestCase):

    def test_Country_initiation(self):
        australia = Country('Australia', 23545500, 7692024)
        andorra = Country('Andorra', 76098, 468)
        madagascar = Country('Madagascar', 26260000, 587000)
        self.assertEqual(australia.is_big, True)
        self.assertEqual(madagascar.is_big, False)
        self.assertEqual(andorra.is_big, False)

    def test_compare_pd(self):
        australia = Country('Australia', 23545500, 7692024)
        andorra = Country('Andorra', 76098, 468)
        brazil = Country('Brazil', 202794000, 8515767)
        china = Country('China', 1393000000, 9597000)
        madagascar = Country('Madagascar', 26260000, 587000)
        self.assertEqual(andorra.compare_pd(australia), "Andorra has a larger population density than Australia")
        self.assertEqual(brazil.compare_pd(china), "Brazil has a smaller population density than China")


