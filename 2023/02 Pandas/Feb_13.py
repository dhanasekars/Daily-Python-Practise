""" 
Created on : 13/02/23 12:23 PM
@author : ds  
"""

import pandas as pd

#   carat	price	shape	clarity	color	cut	        depth	fluorescence	lxwRatio	polish	symmetry	    table
# 0	0.23	250	    Princess	VS1	H	    Good	    74.0	None	        1.01	    Very Good	Good	    81.0
# 1	0.23	250	    Princess	VS1	H	    Good	    77.8    None	        1.00	    Very Good	Good	    71.0
# 2	0.32	253	    Princess	SI2	I	    Very Good	74.7	None	        1.04	    Excellent	Very Good	72.0

# Function to return 5th most common clarity and color combination as a tuple

def get_5th_most_common(df):
    """
    Return the 5th most common clarity and color combination as a tuple
    :param df:
    :return:
    """
    # copilot solution
    return df.groupby(['clarity', 'color']).size().sort_values(ascending=False).index[4]
    # my solution
    # return df.groupby(['clarity','color']).count().sort_values(by='carat',ascending=False).iloc[4].name


# Function for diamonds with carat size between 2 and 2.5 anc cut either Good or Very Good.
# Return the first five results

def get_first_five(df):
    """
    Return the first five diamonds with carat size between 2 and 2.5 anc cut either Good or Very Good.
    :param df:
    :return:
    """
    # copilot solution
    return df[(df.carat.between(2, 2.5)) & (df.cut.isin(['Good', 'Very Good']))].head()
    # my solution
    # return df[df.cut.isin(['Good', 'Very Good']) & (df.carat >= 2) & (df.carat <= 2.5)].head()

