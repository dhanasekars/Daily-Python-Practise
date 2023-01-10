""" 
Created on : 10/01/23 9:37 AM
@author : ds
https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""


def diagonalDifference(arr):
    """
    It is a function that calculates the absolute difference between the sums of its diagonals.
    :param arr: A square matrix
    :return: The absolute difference between the sums of its diagonals
    """
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr) - 1 - i]
    return abs(sum1 - sum2)


