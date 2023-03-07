""" 
Created on : 06/03/23 3:06 PM
@author : ds  
"""


"""
	dept	title	                                hire_date	salary	    sex	    race
0	Police	POLICE SERGEANT	                        2001-12-03 AutomateBoringStuffs	87545.38	Male	White
1	Other	ASSISTANT CITY ATTORNEY II	            2010-11-15	82182.00	Male	Hispanic
2	Houston Public Works	SENIOR SLUDGE PROCESSOR	2006-01-09	49275.00	Male	Black
3	Police	SENIOR POLICE OFFICER	                1997-05-27	75942.10	Male	Hispanic
4	Police	SENIOR POLICE OFFICER	                2006-01-23	69355.26	Male	White
"""

def sex_ratio(df):
    """
    #  Find the percentage of each sex by department. Round to the nearest tenth place
    :return:
    """
    ratios = []

    for dept in range(df.shape[0]):
        # Check if the department has at least one employee. If yes, then continue.
        if df.loc[dept,'sex'] == "":
            continue
        ratio = float(df.loc[dept,'sex']) / float(df.loc[dept, 'department'])
        ratio = round(ratio, 1)
        ratios.append(ratio)

    return ratios
