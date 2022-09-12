""" 
Created on : 11/09/22 3:05 PM
@author : ds  
"""
import collections

test_data = ["A","B"]


def majority_vote(lst):
    try:
        if collections.Counter(lst).most_common(1)[0][1] > len(lst) / 2:
            return collections.Counter(lst).most_common(1)[0][0]
        else:
            return None
    except IndexError:
        return None


# Simple solution which does not need collections, instead use list count()

def majority_vote1(lst):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i


print(majority_vote1(test_data))
