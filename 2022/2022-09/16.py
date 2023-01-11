""" 
Created on : 16/09/22 6:26 PM
@author : ds  
"""

import datetime
test_data = (3, 2000)


def has_friday_13(m, y, d=13):
    return datetime.date(y, m, d).strftime('%A') == 'Friday'


print(has_friday_13(3, 2000))