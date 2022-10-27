""" 
Created on : 27/10/22 7:14 AM
@author : ds  
"""

import re
data = "16/2=8"


def formula(txt):
    result = int(txt.split(sep="=")[1])
    operators = txt.split(sep="=")[0]
    part1 = re.split('/|\*|\+|-', operators)
    part1 = [int(c) for c in part1]
    if '/' in txt:
        output = part1[0] / part1[1]
    elif '*' in txt:
        output = part1[0] * part1[1]
    elif '-' in txt:
        output = part1[0] - part1[1]
    elif '+' in txt:
        output = part1[0] + part1[1]
    return result == output

# Above is first approach
# The below one is after reading about eval()


def eval_formula(txt):
    return eval(txt.split(sep="=")[0]) == int(txt.split(sep="=")[1])


print(eval_formula(data))