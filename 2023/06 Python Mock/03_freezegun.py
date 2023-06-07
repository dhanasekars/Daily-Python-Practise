""" 
Created on : 03/06/23 8:54 am
@author : ds  
"""
from freezegun import freeze_time
import datetime
import unittest


# invoking through decorator pytest style

@freeze_time("2021-07-16")
def test():
    assert datetime.datetime.now() == datetime.datetime(2021, 7, 16)

# invoking through decorator unittest style

@freeze_time("1981-02-01")
class MyTests(unittest.TestCase):
    def test_today(self):
        assert datetime.datetime.now() == datetime.datetime(1981, 2, 1)

# Context Manager

def test():
    assert datetime.datetime.now() != datetime.datetime(1986, 2, 5)
    with freeze_time("1986-02-05"):
        assert datetime.datetime.now() == datetime.datetime(1986, 2, 5)
    assert datetime.datetime.now() != datetime.datetime(1986, 2, 5)
