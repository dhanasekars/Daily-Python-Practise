""" 
Created on : 31/08/22 2:27 PM
@author : ds  
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r_1 = int(input())
# r_2 = int(input())

r_1 = 10
r_2 = 10

min_of_two = min(r_1, r_2)
max_of_two = max(r_1, r_2)


def sum_digits_n_add(n):
    s = 0
    num = n
    while n:
        s += n % 10
        n //= 10
    return num + s


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

while r_1 != r_2:
    if r_1 < r_2:
        r_1 = sum_digits_n_add(r_1)
    else:
        r_2 = sum_digits_n_add(r_2)

print(r_2)