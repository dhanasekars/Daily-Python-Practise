""" 
Created on : 14/11/22 1:16 PM
@author : ds  
"""


# https://edabit.com/challenge/S7rdJsn6vkfC9BzcR


class Employee():
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.name = name.split()[0]
        self.lastname = name.split()[1]


giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(giancarlo.salary)

# Learnings from other solution - use list unpacking
# self.name, self.lastname = name.split()
# using setattr
# for k, v in kwargs.items():
#     setattr(self, k, v)

