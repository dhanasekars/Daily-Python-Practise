"""
Created on : 11/02/23 5:31 AM
@author : ds  
"""


def weekday_hire(df):
    """
    How many employees were hired on a weekday?
    :param df:
    :return:
    """
    df['weekday'] = df['hire_date'].dt.dayofweek
    return df[df['weekday'] < 5].shape[0]


def count_value(df):
    """
    How many total values are in this DataFrame?
    :param df:
    :return:
    """
    return df.size
