""" 
Created on : 29/11/22 5:29 AM
@author : ds  
"""

import unittest
from Nov_29 import CoffeeShop


class test_Coffeeshop(unittest.TestCase):

    def test_CoffeeShop_initiation(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.89},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = CoffeeShop(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.name, "காப்பிக் கடை", [])
        self.assertEqual(shop1.menu, [{"item": "lemonade", "type": "drink", "price": 1.89},
                                      {"item": "hot chocolate", "type": "drink", "price": 2.89},
                                      {"item": "expresso", "type": "drink", "price": 3.89},
                                      {"item": "Americano", "type": "drink", "price": 1.99},
                                      {"item": "bacon", "type": "food", "price": 1.89},
                                      {"item": "ham sandwich", "type": "food", "price": 4.89},
                                      {"item": "steak", "type": "food", "price": 1.99},
                                      {"item": "hamburger", "type": "food", "price": 2.49}])
        self.assertEqual(shop1.orders, [])
        self.assertEqual(shop1.items, ['lemonade', 'hot chocolate', 'expresso', 'Americano', 'bacon', 'ham sandwich',
                                       'steak', 'hamburger'])

    def test_add_order(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.89},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = CoffeeShop(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.add_order("lemonade"), "Order added!")
        self.assertEqual(shop1.add_order("Whisky"), "This item is currently unavailable!")
        self.assertEqual(shop1.orders, ["lemonade"])
