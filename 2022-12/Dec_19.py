""" 
Created on : 19/12/22 1:19 PM
@author : ds
https://edabit.com/challenge/MKpSfBCXargD35J8p
"""


class Taxi:

    def __init__(self, cost):
        self.cost = cost

    def calc_distance(self):
        return round(1 + (self.cost - 3) / 2)

