""" 
Created on : 09/02/23 4:52 AM
@author : ds  
"""

"""
	dept	title	                                hire_date	salary	    sex	    race
0	Police	POLICE SERGEANT	                        2001-12-03	87545.38	Male	White
1	Other	ASSISTANT CITY ATTORNEY II	            2010-11-15	82182.00	Male	Hispanic
2	Houston Public Works	SENIOR SLUDGE PROCESSOR	2006-01-09	49275.00	Male	Black
3	Police	SENIOR POLICE OFFICER	                1997-05-27	75942.10	Male	Hispanic
4	Police	SENIOR POLICE OFFICER	                2006-01-23	69355.26	Male	White
"""


def sex_ratio(df):
    """
    Find the percentage of each sex by department. Round to the nearest tenth place
    :param df:
    :return: df
    """
    # Use count values to get the count of male and female in each department
    s = df.value_counts(['dept', 'sex']).reset_index(name='counts')
    #  Divide group by dept and sex total with group by dept total and multiply by 100
    df = round(s.groupby(['dept', 'sex']).sum() / s.groupby('dept').sum() * 100, 1).reset_index()
    # return the pivot table, using pandas pivot method
    return df.pivot(index='dept', columns='sex', values='counts')
