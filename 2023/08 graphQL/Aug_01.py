""" 
Created on : 01/08 graphQL/23 5:32 am
@author : ds  
"""
import requests


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

