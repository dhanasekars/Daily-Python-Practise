""" 
Created on : 05/04/23 8:51 am
@author : ds  
"""
import pickle
from urllib.request import urlopen
from requests import get

# http://www.pythonchallenge.com/pc/def/peak.html

# pronounce it - peak hell - pickle (package)

# check the data in http://www.pythonchallenge.com/pc/def/banner.p

url = 'http://www.pythonchallenge.com/pc/def/banner.p'


my_beer = pickle.load(urlopen(url))

print(my_beer)

for line in my_beer:
    print("".join([k * v for k, v in line]))

# Solution
# http://www.pythonchallenge.com/pc/def/channel.html
# This is a zip image - may need to use zip