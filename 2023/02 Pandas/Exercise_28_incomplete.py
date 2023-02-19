""" 
Created on : 19/02/23 4:49 AM
@author : ds  
"""

# id	neighborhood	property_type	accommodates	bathrooms	bedrooms	price	security_deposit	cleaning_fee	rating	superhost	response_time	minimum_nights	maximum_nights	latitude	longitude
# 0	3362	Shaw	Townhouse	16	3.5	4	433	500	250	95.0	0	within an hour	2	365	38.90982	-77.02016
# 1	3663	Brightwood Park	Townhouse	4	3.5	4	154	0	50	97.0	0	NaN	3	30	38.95888	-77.02554
# 2	3670	Howard University	Townhouse	2	1.0	1	75	500	25	87.0	0	NaN	2	30	38.91842	-77.02750
# 3	3686	Historic Anacostia	House	1	1.0	1	55	0	0	92.0	0	within a few hours	2	365	38.86314	-76.98836
# 4	3771	Columbia Heights	Other	2	1.0	1	88	0	0	NaN	0	NaN	1	1125	38.92760	-77.03926



# find the distance (in miles) between the centers of each of the top five neighborhoods.
# To calculate distance, use basic Euclidean distance with 360 degrees representing 25,000 miles.
# Sort the final DataFrame by the neighborhood in alphabetical order. Round distance to the nearest tenth of a mile

import numpy as np
import pandas as pd
from math import sqrt
from Feb_18 import neighborhood_stats

def distance_stats(df):
    """
    find the distance (in miles) between all the five centers with latitude and longtitude using basic Euclidean distance.
    Sort the final DataFrame by the neighborhood in alphabetical order. Round distance to the nearest tenth of a mile
    :param df:
    :return:
    """
    df = neighborhood_stats(df)
    df['distance'] = 0
    for i in range(len(df)):
        for j in range(i+1, len(df)):
            df['distance'].iloc[i] = round(sqrt((df['latitude'].iloc[i] - df['latitude'].iloc[j])**2 + (df['longitude'].iloc[i] - df['longitude'].iloc[j])**2) * 25000 / 360, 1)
    return df.sort_values(by='neighborhood')

