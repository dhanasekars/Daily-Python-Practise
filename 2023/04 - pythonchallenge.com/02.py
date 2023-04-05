""" 
Created on : 02/04/23 7:03 am
@author : ds  
"""
# http://www.pythonchallenge.com/pc/def/ocr.html


import re

# Open the text file
with open('02_data.txt', 'r') as file:
    text = file.read()

# Remove all non-alphanumeric characters

new_text = re.sub(r'\W|_+', '', text)
# new_text = re.sub(r'_', '', new_text)

print(new_text)

# Answer is equality, so next challenge here
# http://www.pythonchallenge.com/pc/def/equality.html