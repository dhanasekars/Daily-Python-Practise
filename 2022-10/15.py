""" 
Created on : 15/10/22 9:55 AM
@author : ds  
"""
data = []


def marathon_distance(d):
    """
    Items in the list may be negative or positive,
    but since negative distance isn't possible, find a way to convert negative integers into positive integers.
    :param d:
    :return:
    """
    return sum([abs(i) for i in d]) == 25


print(marathon_distance(data))