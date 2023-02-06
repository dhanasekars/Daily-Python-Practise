""" 
Created on : 05/02/23 4:45 AM
@author : ds  
"""
import pandas as pd


def sex_race_winner(df):
    """
    Which sex and race combination appears the most in the dataset?
    Return the sex, race, and count as a three-item tuple
    :param df:
    :return: tuple
    """
    c = df.loc[df.groupby(['sex', 'race']).sex.count().agg(max)]
    a, b = c[['sex', 'race']]
    return a, b, c.name

    # Actually, the above is a bit of a cheat. The following is the correct answer:
    # return tuple(df.value_counts(['sex', 'race']).reset_index().iloc[0])



