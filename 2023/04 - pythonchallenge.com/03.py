""" 
Created on : 03/04/23 10:08 graphQL am
@author : ds  
"""
# http://www.pythonchallenge.com/pc/def/equality.html


import re

# Open the text file
with open('03_data.txt', 'r') as file:
    text = file.read()

pattern = r"[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"

matches = re.findall(pattern, text)
print(f"matches are {matches}")
print("".join(matches))

# linkedlist
# Level 04 http://www.pythonchallenge.com/pc/def/linkedlist.php