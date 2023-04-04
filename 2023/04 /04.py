""" 
Created on : 04/04/23 11:17 am
@author : ds  
"""
import requests
import re

def linkedlist(num):
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num}'
    r = requests.get(url).text
    pattern = r"and the next nothing is \d+"
    match = re.search(pattern, r)
    next_nothing = r.split()[-1]
    if match:
        print(f"match found {r}")
        print(next_nothing)
        linkedlist(next_nothing)
    else:
        print(f"match not found {r}")


# linkedlist(12345)
# linkedlist(16044/2)
# match found and the next nothing is 66831
# 66831
# match not found peak.html

# http://www.pythonchallenge.com/pc/def/peak.html