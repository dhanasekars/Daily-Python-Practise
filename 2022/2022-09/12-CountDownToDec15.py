""" 
Created on : 12/09/22 9:31 AM
@author : ds  
"""
import datetime

test_date = datetime.datetime(2022, 12, 16)


def count_down(date):
    return str((date - datetime.datetime.today()).days)+' days'


print(count_down(test_date))