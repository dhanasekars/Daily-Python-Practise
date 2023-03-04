""" 
Created on : 03 AutomateBoringStuffs/01/23 7:37 AM
@author : ds
https://www.youtube.com/watch?v=nxjwB8up2gI
"""

import re

values = ["https://www.socratica.com",
          "http://www.socratica.org",
          "file://test.this.path",
          'com.socratica.www_https://']

# Test if strings starts with http or https

regex = 'https?'
for value in values:
    if re.match(regex, value):
        print(value)

# using full match get the first two value alone

regex1 = "https?://w{3}.\w+.(org|com)"
for value in values:
    if re.fullmatch(regex1, value):
        print(value)
