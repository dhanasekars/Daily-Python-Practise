""" 
Created on : 14/02/23 9:46 AM
@author : ds  
"""

#   carat	price	shape	clarity	color	cut	        depth	fluorescence	lxwRatio	polish	symmetry	    table
# 0	0.23	250	    Princess	VS1	H	    Good	    74.0	None	        1.01	    Very Good	Good	    81.0
# 1	0.23	250	    Princess	VS1	H	    Good	    77.8    None	        1.00	    Very Good	Good	    71.0
# 2	0.32	253	    Princess	SI2	I	    Very Good	74.7	None	        1.04	    Excellent	Very Good	72.0

# Find the average price of diamonds per half-carat bin. Automate the process of finding the bins.
# Make the bins exclusive of the start and inclusive of the end. Round the result to the nearest 100.
# The numpy library may help with this challenge

import numpy as np
import pandas as pd

def get_price_per_half_carat(df):
    """
    Return the average price of diamonds per half-carat bin
    :param df:
    :return:
    """
    # copilot solution
    # return df.groupby(pd.cut(df.carat, np.arange(0, df.carat.max() + 0.5, 0.5))).price.mean().round(-2)
    # my solution using helper function
    return df.groupby(pd.cut(df['carat'], bins)).price.mean().round(-2)


# my solution
# Helper function to get the bins
def return_bins(start=0, end=1, split=0.5):
    """
    Return bins for a range of numbers
    :param start: start of range
    :param end: end of range
    :param split: split the range into two parts
    :return: list of bins
    """
    return list(np.arange(start, end + split, split))

df = pd.read_csv('~/data/diamonds2.csv')
bins = return_bins(0, df.carat.max() + 0.5, 0.5)
