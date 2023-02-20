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
    return df[df > 20].resample('D').count().resample('M').count()