""" 
Created on : 15/06/23 5:09 am
@author : ds  
"""
import os
from unittest import skipIf
from nose.tools import assert_dict_contains_subset, assert_is_instance, assert_true
from June_14_services import get_users


BASE_URL = 'http://jsonplaceholder.typicode.com'
# SKIP_TAGS = os.getenv('SKIP_TAGS', '').split()
SKIP_TAGS = 'real'

@skipIf('real' in SKIP_TAGS, 'Skipping tests that hit the real API server.')
def test_request_response():
    response = get_users()

    assert_dict_contains_subset({'Content-Type': 'application/json; charset=utf-8'}, response.headers)
    assert_true(response.ok)
    assert_is_instance(response.json(), list)