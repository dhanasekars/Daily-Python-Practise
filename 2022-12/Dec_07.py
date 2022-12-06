""" 
Created on : 07/12/22 4:50 AM
@author : ds  
"""

# https://edabit.com/challenge/iRvRtg2xxL9BnSEvf

class Person:

    def __init__(self, name: str, likes: list, dislikes: list):
        self.name = name
        self.likes = likes
        self.dislikes = dislikes

    def taste(self, food):
        """
        It will take in a food name as a string.
        Return {person_name} eats the {food_name}.
        If the food is in the person's like list, add 'and loves it!' to the end.
        If it is in the person's hate list, add 'and hates it!' to the end.
        If it is in neither list, simply add an exclamation mark to the end.
        :param food:
        :return: string:
        """
        if food in self.likes:
            add = " and loves it"
        elif food in self.dislikes:
            add = " and hates it"
        else:
            add = ""
        return self.name + " eats the " + food + add + "!"
