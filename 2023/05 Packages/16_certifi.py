""" 
Created on : 06/05/23 6:37 am
@author : ds  
"""

import certifi, requests
import urllib.request

print(certifi.where())
ca_object = urllib.request.urlopen('https://www.google.com', cafile=certifi.where())

# print(certifi.contents())


