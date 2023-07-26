""" 
Created on : 26/07/23 9:35 am
@author : ds  
"""
import random


# Functions and classes are first class citizens
# Anything that can be passed around as regular datatypes

def compose(f, g, x):
    return f(g(x))


compose(print, len, "Hello, World!")


# that can be nested

def random_power():
    def f(x):
        return x ** 2

    def g(x):
        return x ** 3

    def h(x):
        return x ** 4

    functions = [f, g, h]

    return random.choice(functions)


for i in range(10):
    p = random_power()
    print(p(3))
