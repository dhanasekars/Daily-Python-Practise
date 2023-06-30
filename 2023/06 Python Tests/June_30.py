""" 
Created on : 30/06/23 10:30 am
@author : ds  
"""

import random


def generate_password(length):
    if length is int:
        characters = "abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password = ""
        for _ in range(length):
            password += random.choice(characters)
    else:
        return "Error"
    return password


print(generate_password(0.4))
