""" 
Created on : 04/04/23 1:43 pm
@author : ds  
"""
import pickle

beers = ['Bira', 'KF', 'Amstel', 'Tuborg', 'Corona']

with open('beers.pkl', 'wb') as beerpickle:
    pickle.dump(beers, beerpickle)


with open('beers.pkl', 'rb') as beerpickle:
    my_beer = pickle.load(beerpickle)

print(my_beer)