""" 
Created on : 30/11/22 4:53 AM
@author : ds  
"""


from Nov_29 import CoffeeShop


class serveCoffee(CoffeeShop):
    """
    This is class is inherited from Coffeeshop. This class is to serve the orders taken from the Nov_29th class
    """

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
        return round(sum([i["price"] for i in self.menu if i["item"] in self.list_orders()]), 2)

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
