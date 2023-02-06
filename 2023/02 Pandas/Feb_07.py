""" 
Created on : 07/02/23 4:32 AM
@author : ds  
"""
import pandas as pd

def seniority_ratio(df):
    """
    For each department, find the percentage of employees that have the word "senior" as part of their title. Ignore case. Round to the nearest tenths place.
    Return a Series with department as the index. Sort by the index.
    :param df:
    :return:
    """
    # Get the senior count for each department
    seniors = df.loc[df.title.str.contains('senior', case=False)].groupby('dept')['title'].count().sort_index()
    # Get total employees for each department
    total = df.value_counts('dept').sort_index()

    return round(seniors / total * 100, 1)