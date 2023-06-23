""" 
Created on : 23/06/23 11:12 am
@author : ds  
"""
import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return "Hello " + name


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])
