""" 
Created on : 09/06/23 1:52 pm
@author : ds  
"""

from urllib.parse import urljoin
import requests

BASE_URL = 'http://jsonplaceholder.typicode.com'

TODOS_URL = urljoin(BASE_URL, 'todos')

# print(TODOS_URL)

def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None

