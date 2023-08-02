""" 
Created on : 08 graphQL/01/23 2:52 PM
@author : ds
https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

def compareTriplets(a, b):
    """
    It is a function that compares two lists of three elements and give one point to the highest element, zero if equal
    :param a: A triplet of integers
    :param b: A triplet of integers
    :return: score of Alice and Bob
    """
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    return alice, bob

