""" 
Created on : 08 graphQL/02/23 5:12 AM
@author : ds  
"""


def feb_29_count(df):
    """
    How many employees were hired on February 29th?
    :param df:
    :return: integer
    """
    return df.loc[(df.hire_date.dt.day == 29) & (df.hire_date.dt.month == 2)].shape[0]
