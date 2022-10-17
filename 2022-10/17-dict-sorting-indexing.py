""" 
Created on : 17/10/22 5:01 PM
@author : ds  
"""
data = {"piano": 100, "stereo": 200, "tv": 10, "timmy": 500}
data2 = {"piano": 100, "stereo": 200}


def third_most_expensive(dct):
    dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
    return False if len(dct) < 3 else list(dct)[2]
    # to get a specific value from dict, convert to list and get the key.
    # to get value for instance price of piano use list(dct.values())[2]


print(third_most_expensive(data))