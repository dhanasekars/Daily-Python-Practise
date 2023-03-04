""" 
Created on : 10/02/23 5:19 AM
@author : ds  
"""



# 	dept	title	                                 hire_date	 salary	    sex	    race
# 0	Police	POLICE SERGEANT	                        2001-12-03 AutomateBoringStuffs	87545.38	Male	White
# 1	Other	ASSISTANT CITY ATTORNEY II	            2010-11-15	82182.00	Male	Hispanic
# 2	Houston Public Works	SENIOR SLUDGE PROCESSOR	2006-01-09	49275.00	Male	Black
# 3	Police	SENIOR POLICE OFFICER	                1997-05-27	75942.10	Male	Hispanic
# 4	Police	SENIOR POLICE OFFICER	                2006-01-23	69355.26	Male	White


def groupby_tail(df, n=3):
    """
    Return the last n rows of each group.
    :param df:
    :param n:
    :return:
    """
    return df.groupby('dept').tail(n)

def freq(df):
    """
    Count the number of frequency of occurrence of each race within each sex
    :param df:
    :return:
    """
    return df.groupby(['sex', 'race']).count().reset_index().pivot(index='sex',columns='race',values='dept')

def more_title(df):
    """
    Find all the title's that appear in more than one department. Return a set
    :param df:
    :return:
    """
    s = df.groupby('title')['dept'].nunique()
    return set(s[s > 1].index)