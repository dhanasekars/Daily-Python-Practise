"""
Created on : 27/11/22 4:55 AM
@author : ds
"""


# https://edabit.com/challenge/7FyTyi68Df2CxLx6C
# https://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-implement-multiple-constructors

# Create a Pizza class with the attributes order_number and ingredients
# (which is given as a list).Only the ingredients will be given as input.
# You should also make it so that its possible to choose a ready-made pizza flavour
# rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.

class Pizza:
    order_num = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order_num += 1
        self.order_number = Pizza.order_num

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    def ingredients(self):
        return self.ingredients
