""" 
Created on : 03/02/23 4:32 AM
@author : ds  
"""

def median_salary(df):
    """
    Return the median salary  for employees hired from January 1, 2010 onwards. .
    :param df:
    :return: float
    """
    return df[df['hire_date'] >= '2010-01-01'].salary.median()

def hired_in_aug(df):
    """
    Return the number of employees hired in August.
    :param df:
    :return: df
    """
    return df[df['hire_date'].dt.month == 8].groupby(df['hire_date'].dt.year).hire_date.count()

