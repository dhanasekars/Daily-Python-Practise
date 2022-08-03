""" 
Created on : 02/08/22 5:56 PM
@author : ds  
"""
# https://pythonprinciples.com/challenges/Capital-indexes/
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].


def capital_indexes(x):
    j = -1
    output = []
    for i in x:
        j = j+1
        if 64 < ord(i) < 91:
            output.append(j)
    print(output)


capital_indexes("HeLlO")