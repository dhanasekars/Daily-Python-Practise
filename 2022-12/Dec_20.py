""" 
Created on : 20/12/22 5:40 AM
@author : ds
https://edabit.com/challenge/YA5sLYuTzQpWLF8xP
"""


class CleanUp:
    def __init__(self, lst):
        self.lst = lst

    def clean_up_list(self):
        even_list = [i for i in self.lst if not i % 2]
        odd_list = [i for i in self.lst if i % 2]
        return [even_list, odd_list]
