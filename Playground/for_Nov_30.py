""" 
Created on : 30/11/22 5:22 AM
@author : ds  
"""

menu = [{"item": "lemonade", "type": "drink", "price": 1.89},
          {"item": "hot chocolate", "type": "drink", "price": 2.89},
          {"item": "expresso", "type": "drink", "price": 3.89},
          {"item": "Americano", "type": "drink", "price": 1.89},
          {"item": "bacon", "type": "food", "price": 1.99},
          {"item": "ham sandwich", "type": "food", "price": 4.89},
          {"item": "steak", "type": "food", "price": 1.99},
          {"item": "hamburger", "type": "food", "price": 2.49}]

list_order = []


price = sum([i["price"] for i in menu if i["item"] in list_order])

print(price)

cheapest_cost = min([i["price"] for i in menu])
cheapest_item = [i["item"] for i in menu if i["price"] == cheapest_cost]
print(cheapest_item[0])


## --------------------- ##

class CoffeeShop:
    """
    name : a string  - name of the shop
    menu : a list of items( of dict type), with each item containing the item(name of the item) and type(food or drink)
    and price
    orders : an empty list
    """

    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = []
        self.items = [item['item'] for item in menu]  # Fetch  all the items in the menu to a list.

    def add_order(self, user_item):
        """
        adds the name of the item to the end of the orders list if it exists on the menu,
        otherwise, return "This item is currently unavailable!"
        :param user_item:
        :return:
        """
        if user_item in self.items:
            self.orders.append(user_item)
            return "Order added"
        else:
            return "This item is currently unavailable"

    def fulfill_order(self):
        """
        if the orders list is not empty, return "The {item} is ready!".
        If the orders list is empty, return "All orders have been fulfilled!"
        :return: string - A user message.
        """
        if not self.orders:
            return "All orders have been fulfilled!"
        else:
            output_message = "The {} is ready!".format(self.orders[0])
            self.orders.pop(0)
            return output_message

    def list_orders(self):
        """
        returns the item names of the orders taken, otherwise, an empty list.
        :return: a list of running orders
        """
        return self.orders

    def due_amount(self):
        """
        returns the total amount due for the orders taken.
        :return:
        """
        # List comprehension to get price of all the keys of items present in the list_orders
        return sum([i["price"] for i in self.menu if i["item"] in self.list_orders()])

    def cheapest_item(self):
        """
        returns the name of the cheapest item on the menu.
        :return:
        """
        # List comprehension to find the cheapest price
        cheapest_cost = min([i["price"] for i in self.menu])
        # using the cheapest price get the item names
        cheapest_item = [i["item"] for i in self.menu if i["price"] == cheapest_cost]
        return cheapest_item[0]

    def drinks_only(self):
        """
        returns only the item names of type drink from the menu.
        :return: a list of drinks from the menu
        """
        return [i["item"] for i in self.menu if i["type"] == "drink"]

    def food_only(self):
        """
        returns only the item names of type food from the menu.
        :return: a list of food from the menu
        """
        return [i["item"] for i in self.menu if i["type"] == "food"]