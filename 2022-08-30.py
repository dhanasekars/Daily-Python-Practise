""" 
Created on : 30/08/22 11:23 AM
@author : ds  
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
data = [int(i) for i in input().split()]
data = sorted(data, key=abs)
if len(data) == 0:
    print(0)
elif len(data) == 1:
    print(data[0])
else:
    if data[0] + data[1] == 0:
        print(abs(data[0]))
    else:
        print(data[0])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Pythonic solution

input()
T = [int(s) for s in input().split()]
print(T and sorted(sorted(T, reverse=True), key=abs)[0] or 0)
