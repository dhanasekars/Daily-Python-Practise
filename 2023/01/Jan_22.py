""" 
Created on : 22/01/23 4:50 AM
@author : ds
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true
"""

def breakingRecords(scores):
    """
    :param scores: list of integers
    :return: list of integers
    """
    best = scores[0]
    worst = scores[0]
    best_count = 0
    worst_count = 0
    for score in scores:
        if score > best:
            best = score
            best_count += 1
        if score < worst:
            worst = score
            worst_count += 1
    return [best_count, worst_count]