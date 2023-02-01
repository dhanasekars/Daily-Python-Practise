""" 
Created on : 02/02/23 4:35 AM
@author : ds  
"""

# 	dept	title	                                 hire_date	 salary	    sex	    race
# 0	Police	POLICE SERGEANT	                        2001-12-03	87545.38	Male	White
# 1	Other	ASSISTANT CITY ATTORNEY II	            2010-11-15	82182.00	Male	Hispanic
# 2	Houston Public Works	SENIOR SLUDGE PROCESSOR	2006-01-09	49275.00	Male	Black
# 3	Police	SENIOR POLICE OFFICER	                1997-05-27	75942.10	Male	Hispanic
# 4	Police	SENIOR POLICE OFFICER	                2006-01-23	69355.26	Male	White


def dept_salary(df):
    """
    Return the max salary for each department.
    :param df:
    :return:
    """
    return df.loc[df.groupby('dept').salary.idxmax()][["dept", "title", "salary"]] \
        .sort_values(kind='merge_sort', by='salary', ascending=False)
