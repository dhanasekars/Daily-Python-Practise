""" 
Created on : 04/10/22 5:55 AM
@author : ds  
"""

data = ("Russia", 1648195)


def area_of_country(country, area):
    # .format method < python 2.6
    percentage = round(area / 148940000, 4)
    txt = "{} is {:.2%} of the total world's landmass.".format(country, round(area / 148940000, 4))
    new_format = f"{country} is {percentage}% of the total world's landmass"
    # format string literals
    return txt


print(area_of_country(data[0], data[1]))
