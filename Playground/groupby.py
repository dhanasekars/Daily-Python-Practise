""" 
Created on : 10/04/23 11:13 am
@author : ds  
"""

from itertools import groupby

next_seq = "".join([str(len(list(g))) + k for k, g in groupby('13112221')])

print(next_seq)