""" 
Created on : 05/11/22 6:05 AM
@author : ds  
"""

from Nov_05 import histogram


def test_01():
    assert histogram([1, 3, 4], "#") == "#\n###\n####"


def test_02():
    assert histogram([6, 2, 15, 3], "=") == "======\n==\n===============\n==="


def test_03():
    assert histogram([1, 10], "+") == "+\n++++++++++"
