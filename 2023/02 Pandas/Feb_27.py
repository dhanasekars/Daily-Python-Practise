""" 
Created on : 27/02/23 5:42 AM
@author : ds  
"""


def high_low(df):
    """
    Return the 10 highest and lowest temperatures as a Series with the date and city in the index
    :param df:
    :return: series
    """
    df['max_column'] = df.max(axis=1).sort_values(ascending=False)
    df['min_column'] = df.min(axis=1).sort_values()
    return df.head(10)
