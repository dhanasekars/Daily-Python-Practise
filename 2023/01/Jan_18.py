""" 
Created on : 18/01/23 5:36 AM
@author : ds
https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    apple_count = 0
    orange_count = 0
    for apple in apples:
        if s <= a + apple <= t:
            apple_count += 1
    for orange in oranges:
        if s <= b + orange <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)