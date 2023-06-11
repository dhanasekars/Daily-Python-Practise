""" 
Created on : 02/06/23 10:49 am
@author : ds  
"""
import datetime
from unittest.mock import Mock

# assertion mock data
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()
# print(datetime)


def is_weekend():
    today = datetime.datetime.today()
    return today.weekday() > 4


# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
assert not is_weekend()

# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
assert is_weekend()
