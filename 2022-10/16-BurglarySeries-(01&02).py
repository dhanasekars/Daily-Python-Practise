""" 
Created on : 16/10/22 7:20 AM
@author : ds  
"""


data ={
  "tv": 30,
  "skate": 20,
  "stereo": 50,
}


def calculate_losses(items):
    """
    Given a dictionary of the stolen items, return the total amount of the burglary (number).
    If nothing was robbed, return the string "Lucky you!"
    :param items: A dictionary of items
    :return: String or Integer.
    """
    return sum(items.values()) if items else "Lucky you!"


def most_expensive_item(products):
    """
    Given a dictionary of stolen items, return the most expensive item on the items.
    There will be only one most valuable item and dictionary will not be empty.
    :param products: Dictionary of products and its cost
    :return: String
    """
    # return max(products, key=products.get) - A better approach
    return [product for product, value in products.items() if value == max(products.values())][0] # My solution


print(most_expensive_item(data))
