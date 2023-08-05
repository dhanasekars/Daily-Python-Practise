""" 
Created on : 04/08/23 4:46 am
@author : ds  
"""
from me import Operations
import nested
from Aug_01 import setup

query_me = Operations.query.me
query_nested = nested.Operations.query.posts

# print(query_nested)

data = setup.endpoint(query_nested)
print(data)