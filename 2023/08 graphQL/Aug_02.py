""" 
Created on : 02/08/23 6:25 am
@author : ds  
"""

from sgqlc.types import String, Type, Int, ID, Field
from sgqlc.operation import Operation
from Aug_01 import setup
import requests

class UsersNode(Type):
    id = ID
    name = String
    email = String
    age = Int

class Query(Type):
    users = Field(UsersNode)

def test_users_using_sgqlc():
    query = Operation(Query)
    query.users()
    response = requests.post(setup.graphql_endpoint, json={'query': str(query)})
    assert response.status_code == 200
    assert len(response.json()['data']['users']) == 3


test_users_using_sgqlc()