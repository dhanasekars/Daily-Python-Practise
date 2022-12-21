""" 
Created on : 21/12/22 5:07 AM
@author : ds
https://edabit.com/challenge/2XLjgZhmACph76Pkr
"""

class Minimal:
    """
    In this series we're going to see common redundancies and superfluities
    that make our code unnecessarily complicated and less readable, and we're going to learn how to avoid them.
    """
    def __init__(self):
        self.n = None

    def minimal_if(self, n):
        self.n = n
        return not self.n % 2

    def boolean_redundancy(self, n):
        self.n = n
        return ('even', 'odd')[n % 2]