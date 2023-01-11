""" 
Created on : 25/10/22 2:35 PM
@author : ds  
"""

data = ("*PP*RC*S*", "UEAE")


def uncensor(txt, vowels):
    for i in list(vowels):
        txt = txt.replace("*", i, 1)
    return txt


print(uncensor(data[0], data[1]))


