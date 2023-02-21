""" 
Created on : 20/02/23 8:19 AM
@author : ds  
"""

# Count the number of days each month the temperature is above 20 degrees for at least one hour.

def count_days(df):
    """
    Count the number of days each month the temperature is above 20 degrees for at least one hour.
    :param df:
    :return:
    """
    new = df[df > 20].copy().resample('D').nunique()
    new[new != 0] = 1
    return new.resample('M').sum()