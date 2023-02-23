""" 
Created on : 23/02/23 5:18 AM
@author : ds  
"""

import pandas as pd
import numpy as np

# Read the data from the file
df = pd.read_csv('weather_data_austin_2010.csv', index_col='Date', parse_dates=True)

# For the month of June, 2016, find the hour of each day where temperature was the highest.
# Times are in UTC

def highest_hour(df):
    """
    For the month of June, 2016, find the hour of each day where temperature was the highest.
    #idxmax() is depreciated use other methods
    :param df:
    :return:
    """
    [df.loc['2016-06', 'Temperature'].idxmax().hour for i in range(30)]