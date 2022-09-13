""" 
Created on : 13/09/22 4:11 PM
@author : ds  
"""

def loves_me(n):
    odd_days = 'Loves me,'
    even_days = 'Loves me not,'
    output = ""
    for i in range(1, n+1):
        if i == n:
            if n % 2 == 1:
                output = output + " " + odd_days[:-1].upper()
            else:
                output = output + " " + even_days[:-1].upper()

        elif i % 2 == 1:
            output = output + " " + odd_days
        else:
            output = output + " " + even_days

    return output.strip()


print(loves_me(3))

# Pythonic solution


def loves_me_pythonic(n):
    arr = (['Loves me', 'Loves me not']*n)[:n]
    arr[-1] = arr[-1].upper()
    return ', '.join(arr)