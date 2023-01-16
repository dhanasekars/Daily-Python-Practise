""" 
Created on : 16/01/23 8:50 AM
@author : ds
https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""

def birthdayCakeCandles(candles):
    """
    It is a function that calculates the number of candles that can be blown out
    :param candles: A list of integers
    :return: The number of candles that can be blown out
    """
    return candles.count(max(candles))