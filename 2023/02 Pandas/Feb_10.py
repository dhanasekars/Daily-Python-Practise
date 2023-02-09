""" 
Created on : 10/02/23 5:19 AM
@author : ds  
"""

def groupby_tail(df, n=3):
    """
    Return the last n rows of each group.
    :param df:
    :param n:
    :return:
    """
    return df.groupby('dept').tail(n)

