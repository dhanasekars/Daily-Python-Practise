""" 
Created on : 27/04/23 7:11 am
@author : ds  
"""
import keyword

for kw in keyword.kwlist:
    print(kw)

print(keyword.iskeyword('try'))