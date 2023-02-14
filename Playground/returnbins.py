""" 
Created on : 14/02/23 10:00 AM
@author : ds  
"""
import numpy as np

def return_bins(start=0, end=1, split=0.5):
    """
    Return bins for a range of numbers
    :param start: start of range
    :param end: end of range
    :param split: split the range into two parts
    :return: list of bins
    """
    # copilot solution
    return list(np.arange(start, end + split, split))
    # my solution


# helper function to get the bins



print(return_bins(0,14,0.5))