""" 
Created on : 06/11/22 5:32 AM
@author : ds  
"""

data = ""


def split(txt):
    """
    Write a function that groups a string into parentheses clusters.
    Each cluster should be balanced.
    :param txt: string of parentheses
    :return: list : separated balanced parentheses cluster
    """
    if txt != '':
        output = ""
        score = 0
        for c in txt:
            if c == '(':
                score += 1
            elif c == ')':
                score += -1
            if score != 0:
                output = output + c
            elif score == 0:
                output = output + c
                output = output + ','
        return output.strip(',').split(',')
    else:
        return []


print(split(data))