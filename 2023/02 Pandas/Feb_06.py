""" 
Created on : 06/02/23 6:35 AM
@author : ds  
"""

import pandas as pd

def increasing_salary(df):
    """
    Return a DataFrame of strictly increasing salaries. Do this without rearranging row order,
    but by filtering out any employee who does not have a salary greater than the employee above them    :param df:
    :return: pd.dataframe
    """
    df = df.dropna(subset=['salary'])
    sal = df['salary']
    return df[sal > sal.cummax().shift().fillna(0)]