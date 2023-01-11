""" 
Created on : 01/12/22 4:49 AM
@author : ds  
"""


# https://edabit.com/challenge/m9zn9v3Q6oG8zBdja

class Memories:
    """
    Hello there, I seem to not remember who I am, my memories is all cloudy, although maybe if I could piece it together
    Oh! Maybe you could help me make a class that helps me remember things.
    Maybe a method called add that would add to my memory if I would recall things
    and a remember method that would let me recall a specific memory. But you have to make add more flexible,
    I might recall many things in an instant or only one that I would forget again.
    """
    memory = {}

    def add_my_solution(self, **kwargs):
        self.__dict__.update(kwargs)
        self.memory = {key: value for key, value in self.__dict__.items()}
        return self.memory

    def remember_my_solution(self, recover):
        return self.memory.get(recover) if self.memory.get(recover) else False

    # Better solution from others
    def add(self, **kwargs):
        self.memory.update(kwargs)

    def remember(self, thing):
        return self.memory.get(thing, False)



