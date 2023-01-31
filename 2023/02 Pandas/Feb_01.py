""" 
Created on : 01/02/23 4:03 AM
@author : ds  
"""

"""
    dept	  title	                                  hire_date	salary	    sex	    race
0	Police	POLICE SERGEANT	                        2001-12-03	87545.38	Male	White
1	Other	ASSISTANT CITY ATTORNEY II	            2010-11-15	82182.00	Male	Hispanic
2	Houston Public Works	SENIOR SLUDGE PROCESSOR	2006-01-09	49275.00	Male	Black
3	Police	SENIOR POLICE OFFICER	                1997-05-27	75942.10	Male	Hispanic
4	Police	SENIOR POLICE OFFICER	                2006-01-23	69355.26	Male	White

"""

def select_data(df):
    """
    Select the first five rows for columns title and salary.
    :param df: dataframe
    :return: dataframe
    """
    return df[['title', 'Salary']][:5]

def select_movie(df):
    """
    Select the year, content_rating, and duration columns for all movies between
    "The Lion King" and "The Little Prince".
    :param df:
    :return:
    """
    return df.loc['The Lion King':'The Little Prince', ['year', 'content_rating', 'duration']]

def select_hundreth(df):
    """
    Select every 100th row beginning with the first row
    :param df:
    :return:
    """
    return df.iloc[::100]

def select_sort(df):
    """
    Return the first 10 employees hired from March 1, 2010. Use `kind="mergesort"` if sorting.
    :param df:
    :return:
    """
    return df[df['hire_date'] >= '2010-03-01'].sort_values(by='hire_date', kind='merge_sort')[:10]