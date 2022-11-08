""" 
Created on : 07/11/22 5:59 AM
@author : ds  
"""


# https://edabit.com/challenge/9cNxcMjfEMzKYoBZY

# Given a positive number x, if all the positive divisors of x (excluding x)
# add up to x, then x is said to be a perfect number.For example,
# the set of positive divisors of 6 excluding 6 itself is (1, 2, 3).
# The sum of this set is 6. Therefore, 6 is a perfect number.
# Given a positive number x, if all the positive divisors of x add up to a second number y,
# and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.

def num_type(n):
    def sum_of_divisors(num):
        lst = []
        for i in range(1, num):
            if not num % i:
                lst.append(i)
        return sum(lst)

    sum_ = sum_of_divisors(n)
    if sum_ == n:
        return 'Perfect'
    elif sum_of_divisors(sum_) == n:
        return 'Amicable'
    else:
        return 'Neither'


print(num_type(2924))

# Lamda function
# 	div_sum = lambda n: sum(i for i in range(1,n) if n%i == 0)
