""" 
Created on : 27/04/23 7:55 am
@author : ds  
"""

# https://curl.se

# https://curlconverter.com

import pycurl
import certifi
from io import BytesIO

buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, "http://pycurl.io/")
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))

# for i in {1..25}; do curl -u butter:fly -o wave$i.wav http://www.pythonchallenge.com/pc/hex/lake$i.wav; done