""" 
Created on : 15/02/23 11:31 AM
@author : ds  
"""


# carat	price	shape	clarity	color	cut	        depth	fluorescence	lxwRatio	polish	symmetry	    table
# 0	0.23	250	    Princess	VS1	H	    Good	    74.0	None	        1.01	    Very Good	Good	    81.0
# 1	0.23	250	    Princess	VS1	H	    Good	    77.8    None	        1.00	    Very Good	Good	    71.0
# 2	0.32	253	    Princess	SI2	I	    Very Good	74.7	None	        1.04	    Excellent	Very Good	72.0
# 3	0.30	271	    Princess	VS1	I	    Very Good	74.0	None	        1.03	    Excellent	Good	    74.0
# 4	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0
# 5	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0
# 6	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0
# 7	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0
# 8	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0
# 9	0.30	272	    Princess	SI1	I	    Very Good	72.4	Faint	        1.01	    Excellent	Very Good	68.0


def filter_diamond(df):
    """
    Filter for the diamonds that have the same cut, polish and symmetry. Return the last 10 results.
    :param df:
    :return:
    """
    return df.sort_values(by=['cut', 'polish', 'symmetry']).tail(10)

