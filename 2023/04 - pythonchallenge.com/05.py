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


r = pickle.load(urlopen(url))

print(r)

for line in r:
    print("".join([k * v for k, v in line]))

# Solution
# http://www.pythonchallenge.com/pc/def/channel.html
# This is a zip image - may need to use zip