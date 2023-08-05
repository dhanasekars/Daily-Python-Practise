""" 
Created on : 01/08 graphQL/23 5:32 am
@author : ds  
"""
import requests
from sgqlc.endpoint.http import HTTPEndpoint


class setup:
    graphql_endpoint = "http://localhost:4000"
    payload = """ {
        posts {
            id
            title
            body
            published
        }
    }"""
    endpoint = HTTPEndpoint("http://localhost:4000")

