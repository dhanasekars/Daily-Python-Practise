""" 
Created on : 17/01/23 5:47 AM
@author : ds
https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true
"""

# Complete the formingMagicSquare function below.

def formingMagicSquare(s):
    # 8 possible magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    # calculate the cost of each magic square
    costs = []
    for magic_square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(magic_square[i][j] - s[i][j])
        costs.append(cost)

    # return the minimum cost
    return min(costs)
