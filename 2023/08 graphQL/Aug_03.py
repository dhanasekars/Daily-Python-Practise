""" 
Created on : 03/08/23 5:04 am
@author : ds  
"""
from sgqlc.operation import Operation
from instrospection_schema import instrospection_schema as schema
from Aug_01 import setup
from sgqlc.endpoint.http import HTTPEndpoint


endpoint = HTTPEndpoint(setup.graphql_endpoint)
op = Operation(schema.Query)

# select fields
post = op.posts()
author = op.posts.author()

# select fields by *args
author.__fields__('name', 'email', 'age')

# select fields using **kwargs
post.__fields__(body=True, title=True)

# print the graphql generated using Operation
print(op)

# call the endpoint passing the query
data = endpoint(op)
print(data)

# converting the json to native objects
result = (op + data).posts
print(result)

for post in result:
    print(post.author.name)
    print(post.title)