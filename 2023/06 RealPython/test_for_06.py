""" 
Created on : 06/06/23 10:34 am
@author : ds  
"""
import unittest
from June_06_my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch


class TestCalendar(unittest.TestCase):
    @patch('June_06_my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()

if __name__ =='__main__':
    unittest.main()





