""" 
Created on : 22/02/23 5:25 AM
@author : ds  
"""
#                     Seattle	San Francisco	Los Angeles	Las Vegas	Denver	Houston	Chicago	Atlanta	Miami	New York
# datetime
# 2013-01-01 00:00:00	2.94	11.50	11.66	7.28	-2.30	8.81	-0.19	1.92	19.41	-1.12
# 2013-01-01 01:00:00	2.40	10.22	10.67	5.95	-3.23	8.81	0.28	0.60	19.35	-1.69
# 2013-01-01 02:00:00	1.70	8.02	9.91	5.18	-3.03 AutomateBoringStuffs	8.81	0.33	-0.53	18.99	-1.96
# 2013-01-01 03 AutomateBoringStuffs:00:00	1.45	7.30	9.33	4.42	-3.67	8.48	0.12	-1.36	18.56	-2.08
# 2013-01-01 04:00:00	0.95	6.84	8.82	3.62	-5.55	8.34	0.04	-1.44	18.49	-2.32


# Calculate the median temperature at 3 p.m. every 6 month period for each city.
# Use January 1 - June 30, 2013 as the fist period. Round to the nearest tenth.


def median_temp(df):
    """
    Calculate the median temperature at 3 p.m. every 6 month period for each city.
    :param df:
    :return:
    """
    return df.loc[df.index.hour == 15].resample('6MS').median().round(1)
