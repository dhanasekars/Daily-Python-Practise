""" 
Created on : 29/11/22 5:29 AM
@author : ds  
"""

# menu = [{"item": "lemonade", "type": "drink", "price": 1.89},
#           {"item": "hot chocolate", "type": "drink", "price": 2.89},
#           {"item": "expresso", "type": "drink", "price": 3.89},
#           {"item": "Americano", "type": "drink", "price": 1.99},
#           {"item": "bacon", "type": "food", "price": 1.89},
#           {"item": "ham sandwich", "type": "food", "price": 4.89},
#           {"item": "steak", "type": "food", "price": 1.99},
#           {"item": "hamburger", "type": "food", "price": 2.49}]


class CoffeeShop:
    """
    name : a string  - name of the shop
    menu : a list of items( of dict type), with each item containing the item(name of the item) and type(food or drink)
    and price
    orders : an empty list
    """

    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []
        self.items = [item['item'] for item in menu]

    def add_order(self, user_item):
        if user_item in self.items:
            self.orders.append(user_item)
            return "Order added"
        else:
            return "This item is currently unavailable"


