""" 
Created on : 10/04/23 10:52 am
@author : ds  
"""


# This is look and say sequence


# from itertools import groupby
# next_seq = "".join([str(len(list(g))) + k for k, g in groupby('13112221')])
# print(next_seq)

def look_and_say(n):
    """Generate the n-th Look-and-Say sequence."""
    if n == 1:
        return "1"
    prev_seq = look_and_say(n-1)
    seq = ""
    i = 0
    while i < len(prev_seq):
        digit = prev_seq[i]
        count = 1
        while i + 1 < len(prev_seq) and prev_seq[i + 1] == digit:
            count += 1
            i += 1
        seq += str(count) + digit
        i += 1
    return seq


print(len(look_and_say(31)))


# http://www.pythonchallenge.com/pc/return/5808.html