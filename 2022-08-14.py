"""
Created on : 14/08/22 6:27 PM
@author : ds  
"""


def get_row_col(s):
    translate = {"A":0, "B":1, "C":2}
    letter = s[0]
    number = s[1]
    row = int(number) - 1
    column = translate[letter]
    return row, column


print(get_row_col("A3"))
