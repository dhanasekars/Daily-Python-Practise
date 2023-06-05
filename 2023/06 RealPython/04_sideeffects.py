""" 
Created on : 05/06/23 9:36 am
@author : ds  
"""
import unittest

import requests
from unittest.mock import Mock
from requests.exceptions import Timeout

requests = Mock()


def get_holidays():
    r = requests.get("http://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()


class TestSideEffects(unittest.TestCase):
    def log_request(self, url):
        print(f'Making a request to {url}.')
        print(f'Request Received.')

        # Mock response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'


if __name__ == '__main__':
    unittest.main()
