""" 
Created on : 30/11/22 4:53 AM
@author : ds  
"""

import unittest
from Nov_30 import serveCoffee


class test_serveCoffee(unittest.TestCase):

    def test_fulfill_order(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.89},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.fulfill_order(),"All orders have been fulfilled!")
        shop1.add_order("hamburger")
        self.assertEqual(shop1.fulfill_order(),"The hamburger is ready!")
        self.assertEqual(shop1.orders, [])

    def test_list_orders(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.89},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.list_orders(), [])
        shop1.add_order("hamburger")
        shop1.add_order("bacon")
        shop1.add_order("Americano")
        self.assertEqual(shop1.orders, ["hamburger", "bacon", "Americano"])
        shop1.fulfill_order()
        self.assertEqual(shop1.orders, ["bacon", "Americano"])
        shop1.fulfill_order()
        self.assertEqual(shop1.orders, ["Americano"])
        shop1.fulfill_order()
        self.assertEqual(shop1.orders, [])

    def test_due_amount(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.89},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.list_orders(), [])
        self.assertEqual(shop1.due_amount(), 0.0)
        shop1.add_order("hamburger")
        self.assertEqual(shop1.due_amount(), 2.49)
        shop1.add_order("bacon")
        shop1.add_order("Americano")
        self.assertEqual(shop1.due_amount(), 6.37)
        shop1.fulfill_order()
        self.assertEqual(shop1.due_amount(), 3.88)

    def test_cheapest_item(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.99},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.cheapest_item(), "lemonade")

    def test_drinks_only(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.99},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.drinks_only(), ["lemonade", "hot chocolate", "expresso", "Americano"])

    def test_food_only(self):
        menu1 = [{"item": "lemonade", "type": "drink", "price": 1.89},
                 {"item": "hot chocolate", "type": "drink", "price": 2.89},
                 {"item": "expresso", "type": "drink", "price": 3.89},
                 {"item": "Americano", "type": "drink", "price": 1.99},
                 {"item": "bacon", "type": "food", "price": 1.99},
                 {"item": "ham sandwich", "type": "food", "price": 4.89},
                 {"item": "steak", "type": "food", "price": 1.99},
                 {"item": "hamburger", "type": "food", "price": 2.49}]
        shop1 = serveCoffee(name="காப்பிக் கடை", menu=menu1, orders=[])
        self.assertEqual(shop1.food_only(), ["bacon", "ham sandwich", "steak", "hamburger"])