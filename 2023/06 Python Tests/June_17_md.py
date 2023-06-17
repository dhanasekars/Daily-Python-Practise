""" 
Created on : 17/06/23 10:36 am
@author : ds  
"""
import re

import markdown

with open('floating point.md', 'r') as file:
    markdown_text = file.read()

pattern = r"```([\s\S]*?)```"

# Find all matches

matches = re.findall(pattern, markdown_text)

#Print the pattern

for match in matches:
    print(match)