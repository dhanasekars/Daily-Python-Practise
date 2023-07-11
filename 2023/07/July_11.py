""" 
Created on : 11/07/23 8:53 am
@author : ds  
"""


# Decorators

# First class functions

def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_fun):
    return greeter_fun("Bob")


print(greet_bob(say_hello))
print(greet_bob(be_awesome))
