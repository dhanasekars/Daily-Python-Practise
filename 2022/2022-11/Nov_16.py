""" 
Created on : 15/11/22 6:01 AM
@author : ds  
"""


# https://edabit.com/challenge/ta8GBizBNbRGo5iC6


class Calculator:
    """
    Create methods for the Calculator class that can do the following:
    Add two numbers.
    Subtract two numbers.
    Multiply two numbers.
    Divide two numbers.
    """

    # since argument is passed to the class method,
    # should not initiate variables in the init method
    # or have it initiated to none as per PEP8
    # def __init__(self):
    #     self.n2 = None
    #     self.n1 = None

    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def subtract(n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 * self.n2

    def divide(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 / self.n2


c = Calculator()

print(c.add(1, 6))
