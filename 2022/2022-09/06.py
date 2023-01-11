""" 
Created on : 06/09/22 3:44 PM
@author : ds  
"""

lost_items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
}


def find_it(items, name):
    name_title = name.title()
    if name in items:
        return "{} is gone...".format(name_title)
    else:
        return "{} is here!".format(name_title)


print(find_it(lost_items, 'timmy4'))




