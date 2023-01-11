""" 
Created on : 02/01/23 6:23 AM
@author : ds
https://www.youtube.com/watch?v=BfS2H1y6tzQ
"""

import random


def random_walk(n):
    """Return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y


# Monte Carlo simulation

number_of_walks = 20000

for walk_length in range(1, 101):
    no_transport = 0  # number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)
