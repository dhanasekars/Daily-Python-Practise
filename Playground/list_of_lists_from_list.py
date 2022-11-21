""" 
Created on : 21/11/22 7:43 AM
@author : ds  
"""
import numpy as np

items = list("abcde")
pagesize = 1


pages = [items[i * pagesize:(i + 1) * pagesize] for i in range((len(items) + pagesize - 1) // pagesize)]

print(pages)





