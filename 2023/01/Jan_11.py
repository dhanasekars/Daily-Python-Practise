""" 
Created on : 11/01/23 9:34 AM
@author : ds
https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

def plusMinus(arr):
    """
    It is a function that calculates the fraction of positive, negative and zero numbers in a list
    :param arr: A list of integers
    :Print the ratios of positive, negative and zero values in the array.
    Each value should be printed on a separate line with  digits after the decimal.
    The function should not return a value.
    """
    positive, negative, zero = 0, 0, 0  # Initialize the variables
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    # print(f"{positive / len(arr):.6f}")
    # print(f"{negative / len(arr):.6f}")
    # print(f"{zero / len(arr):.6f}")

    return [f"{positive / len(arr):.6f}", f"{negative / len(arr):.6f}", f"{zero / len(arr):.6f}"]

