""" 
Created on : 19/02/23 5:30 AM
@author : ds  
"""

# id	neighborhood	property_type	accommodates	bathrooms	bedrooms	price	security_deposit	cleaning_fee	rating	superhost	response_time	minimum_nights	maximum_nights	latitude	longitude
# 0	3362	Shaw	Townhouse	16	3.5	4	433	500	250	95.0	0	within an hour	2	365	38.90982	-77.02016
# 1	3663	Brightwood Park	Townhouse	4	3.5	4	154	0	50	97.0	0	NaN	3	30	38.95888	-77.02554
# 2	3670	Howard University	Townhouse	2	1.0	1	75	500	25	87.0	0	NaN	2	30	38.91842	-77.02750
# 3	3686	Historic Anacostia	House	1	1.0	1	55	0	0	92.0	0	within a few hours	2	365	38.86314	-76.98836
# 4	3771	Columbia Heights	Other	2	1.0	1	88	0	0	NaN	0	NaN	1	1125	38.92760	-77.03926


def total_cost(df):
    """
    Calculate the total cost of each listing as the sum of the price, security deposit and cleaning fee.
    Return a DataFrame of the cost columns plus the total for the first 10 rows.
    :param df:
    :return:
    """
    new_df = df.head(10)
    new_df['total'] = new_df.price + new_df.security_deposit + new_df.cleaning_fee
    return new_df[['price', 'security_deposit', 'cleaning_fee', 'total']]
    # copilot suggestion
    # return df[['price', 'security_deposit', 'cleaning_fee']].sum(axis=1).head(10)