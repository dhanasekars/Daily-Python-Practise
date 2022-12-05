""" 
Created on : 06/12/22 4:33 AM
@author : ds  
"""

# https://edabit.com/challenge/smLmHK89zNoeaDSZp

class Country:

    def __init__(self, name, population, area, is_big=False):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = True if self.area > 250000000 or area > 3000000 else is_big

    def compare_pd(self, other):
        if self.population / self.area > other.population / other.area:
            return "{} has a larger population density than {}".format(self.name, other.name)
        else:
            return "{} has a smaller population density than {}".format(self.name, other.name)

# Representing millions in e power
# 25e7 3e6
# result = ['smaller', 'larger'][self.density > other.density]
