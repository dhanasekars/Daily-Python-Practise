""" 
Created on : 04/02/23 4:41 AM
@author : ds  
"""

def reg_match(df):
    """
    Return the number of employees from the "Police" department that do not have the word "police" in their title.
    Ignore case.
    :param df:
    :return: df
    """
    return df.loc[(df.dept == 'Police') & ~(df.title.str.contains('police', case=False))].shape[0]

