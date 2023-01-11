""" 
Created on : 03/11/22 5:40 AM
@author : ds  
"""
from Nov_02 import discount


def test_02():
    assert discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) \
           == [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]
    assert discount([10.75, 11.68]) == [10.75, 11.68]
    assert discount([68.74, 17.85, 55.99]) == [60.13, 15.62, 48.98]