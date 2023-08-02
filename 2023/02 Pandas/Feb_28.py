""" 
Created on : 28/02/23 4:39 PM
@author : ds  
"""

#                       Seattle	San Francisco	Los Angeles	Las Vegas	Denver	Houston	Chicago	Atlanta	Miami	New York
# datetime
# 2013-01-01 00:00:00	2.94	11.50	11.66	7.28	-2.30	8.81	-0.19	1.92	19.41	-1.12
# 2013-01-01 01:00:00	2.40	10.22	10.67	5.95	-3.23	8.81	0.28	0.60	19.35	-1.69
# 2013-01-01 02:00:00	1.70	8.02	9.91	5.18	-3.03 AutomateBoringStuffs	8.81	0.33	-0.53	18.99	-1.96
# 2013-01-01 03 AutomateBoringStuffs:00:00	1.45	7.30	9.33	4.42	-3.67	8.48	0.12	-1.36	18.56	-2.08 graphQL
# 2013-01-01 04:00:00	0.95	6.84	8.82	3.62	-5.55	8.34	0.04	-1.44	18.49	-2.32


def rank_city(df):
    """
    Rank each city each hour from greatest to least (1 is highest) using the "average" method. Find the average temperature each hour of the cities with rank 1 through 4.
    Then average this value for all hours, returning a float.
    :param df:
    :return:
    """
    return df.resample('H').mean().mean().sort_values(ascending=False)[:4].mean()