"""
Created on : 26/12/22 5:41 AM
@author : ds
https://edabit.com/challenge/8vBvgJMc2uQJpD6d7
"""


def prime_factors(num):
    result = []
    for i in range(2, int(num**0.5) + 1):
        while not num % i:
            result.append(i)
            num //= i
    return result + [num] if num > 1 else result
