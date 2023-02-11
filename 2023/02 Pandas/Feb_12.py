""" 
Created on : 12/02/23 4:43 AM
@author : ds  
"""

#   carat	price	shape	clarity	color	cut	        depth	fluorescence	lxwRatio	polish	symmetry	    table
# 0	0.23	250	    Princess	VS1	H	    Good	    74.0	None	        1.01	    Very Good	Good	    81.0
# 1	0.23	250	    Princess	VS1	H	    Good	    77.8    None	        1.00	    Very Good	Good	    71.0
# 2	0.32	253	    Princess	SI2	I	    Very Good	74.7	None	        1.04	    Excellent	Very Good	72.0
# 3	0.30	271	    Princess	VS1	I	    Very Good	74.0	None	        1.03	    Excellent	Good	    74.0
# 4	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0


def filter_diamond(df):
    """
    Select all with color E and clarity IF
    :param df:
    :return:
    """
    return df[(df.color == 'E') & (df.clarity == 'IF')]

def price_filter(df):
    """
    Select all with price per carat > 50000
    :param df:
    :return:
    """
    return df[df.price / df.carat > 50000]