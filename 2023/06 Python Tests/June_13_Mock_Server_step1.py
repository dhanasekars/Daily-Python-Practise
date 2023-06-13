""" 
Created on : 13/06/23 12:45 pm
@author : ds  
"""

from nose.tools import assert_true, assert_is_not_none
import requests
from June_09_services import get_todos
BASE_URL = 'http://jsonplaceholder.typicode.com'

def test_request_response():
    response = get_todos()
    assert_is_not_none(response.ok)