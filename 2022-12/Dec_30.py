""" 
Created on : 30/12/22 5:30 AM
@author : ds
https://www.youtube.com/watch?v=LosIGgon_KM
"""

import urllib
from urllib import request

url = "https://www.dhanasekars.com"

# req = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
# resp = urllib.request.urlopen(req)
# data = resp.read()
# html = data.decode("UTF-8")
# print(resp.code)
# print(len(data))
# # print(html)


# using parse module

from urllib import parse

params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
url = "https://youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
print(resp.code)
# read and decode the response
html = resp.read().decode("utf-8")
print(html[0:500])