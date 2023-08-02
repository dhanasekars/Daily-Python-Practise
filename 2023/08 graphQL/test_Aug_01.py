""" 
Created on : 01/08 graphQL/23 5:48 am
@author : ds  
"""
from Aug_01 import setup
import unittest
import requests


def test_status_code_200():
    response = requests.post(setup.graphql_endpoint, json={'query': setup.payload})
    response_body = response.json()
    assert response.status_code == 200
    print(response_body['data']['posts'][0]['title'])
    assert response_body['data']['posts'][0]['title'] == 'GraphQL 101'


test_status_code_200()
