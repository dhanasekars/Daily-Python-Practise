""" 
Created on : 17/04/23 10:21 am
@author : ds  
"""
import urllib.request
from urllib.request import urlopen, Request
from urllib.parse import unquote_plus, unquote_to_bytes,quote_plus
from xmlrpc.client import ServerProxy

import re
import bz2
import xmlrpc.client

# url = "http://www.pythonchallenge.com/pc/return/romance.html"
# cookie = None
# info = ""
# num = '12345'
#
# # follow busynothing and collect cookies
#
# while True:
#     h = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + num)
#     response = h.read().decode()
#     # print(response)
#     cookie = h.getheader("Set-Cookie")
#     info += re.search('info=(.*?);', cookie).group(1)
#     match = re.search(r'the next busynothing is (\d+)', response)
#     if match is None:
#         break
#     else:
#         num = match.group(1)
#
# res = unquote_to_bytes(info.replace("+", " "))
# # print(res)
# print(bz2.decompress(res).decode())
#  is it the 26th already?
#  call his father and inform him that "the flowers are on their way". he'll understand.


# conn = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
# print(conn.phone("Leopold"))


url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers={ "Cookie": "info=" + quote_plus(msg)})

print(urlopen(req).read().decode())

# <html>
# <head>
#   <title>it's me. what do you want?</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# 	<br><br>
# 	<center><font color="gold">
# 	<img src="leopold.jpg" border="0"/>
# <br><br>
# </font>
# </body>
# </html>

#  http://www.pythonchallenge.com/pc/return/balloons.html