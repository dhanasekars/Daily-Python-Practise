""" 
Created on : 19/01/23 5:22 AM
@author : ds
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
"""

def timeConversion(s):
    # Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    if s[8:] == "PM":
        if s[:2] == "12":
            return s[:8]
        else:
            return str(int(s[:2]) + 12) + s[2:8]
    else:
        if s[:2] == "12":
            return "00" + s[2:8]
        else:
            return s[:8]