""" 
Created on : 26/08/22 5:39 PM
@author : ds  
"""


def generation(x, y):
    male = {-3: "great grandfather", -2: "grandfather", -1: "father", 0: "me!", 1: "son",
            2: "grandson", 3: "great grandson"}
    female = {-3: "great grandmother", -2: "grandmother", -1: "mother", 0: "me!", 1: "daughter",
            2: "granddaughter", 3: "great granddaughter"}
    return male[x] if y == 'm' else female[x]


print(generation(0, 'm'))

