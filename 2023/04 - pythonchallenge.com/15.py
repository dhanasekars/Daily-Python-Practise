""" 
Created on : 15/04/23 12:34 pm
@author : ds  
"""
# http://www.pythonchallenge.com/pc/return/uzi.html


import datetime, calendar


for year in range(1006, 1996, 10):
    d = datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print(d)


#  So the answer is 1756-01-26

