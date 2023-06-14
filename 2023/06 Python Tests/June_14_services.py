""" 
Created on : 14/06/23 4:36 am
@author : ds  
"""
from urllib.parse import urljoin
import requests


BASE_URL = 'http://jsonplaceholder.typicode.com'


USERS_URL = urljoin(BASE_URL, 'users')

def get_users():
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None
