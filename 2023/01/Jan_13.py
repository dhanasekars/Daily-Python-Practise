""" 
Created on : 13/01/23 11:01 AM
@author : ds
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

def miniMaxSum(arr):
    """
    It is a function that calculates the minimum and maximum sum of four of the five integers
    :param arr: A list of five integers
    :Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
    The function should not return a value.
    """
    arr.sort()
    return [sum(arr[:4]), sum(arr[1:])]