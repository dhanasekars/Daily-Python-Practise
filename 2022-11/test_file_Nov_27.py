""" 
Created on : 27/11/22 4:55 AM
@author : ds  
"""

import unittest
from Nov_27_multiple_constructor import Pizza


class test_Pizza(unittest.TestCase):

    def test_order_no(self):
        p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
        p2 = Pizza.meat_festival()  # order 2
        p4 = Pizza.hawaiian()  # order 2

        self.assertEqual(p1.order_number, 1)
        self.assertEqual(p2.order_number, 2)
        self.assertEqual(p4.order_number, 3)

    def test_ready_made_ingredients(self):
        p1 = Pizza.meat_festival()  # order 2
        p2 = Pizza.hawaiian()  # order 2
        self.assertEqual(p1.ingredients, ["beef", "meatball", "bacon"])
        self.assertEqual(p2.ingredients, ["ham", "pineapple"])

    def test_custom_made_ingredients(self):
        p1 = Pizza(["bacon", "parmesan", "ham"])  # order 2
        p2 = Pizza(["bacon", "beef", "ham", "pineapple"])  # order 2
        self.assertEqual(p1.ingredients, ["bacon", "parmesan", "ham"])
        self.assertEqual(p2.ingredients, ["bacon", "beef", "ham", "pineapple"])