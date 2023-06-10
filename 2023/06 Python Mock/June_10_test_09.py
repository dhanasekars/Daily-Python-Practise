""" 
Created on : 10/06/23 7:18 am
@author : ds  
"""

from nose.tools import assert_is_not_none
from June_09_services import get_todos
from unittest.mock import Mock, patch

@patch('June_09_services.requests.get')
def test_request_response(mock_get):
    mock_get.return_value.ok = True
    response = get_todos()
    assert_is_not_none(response)