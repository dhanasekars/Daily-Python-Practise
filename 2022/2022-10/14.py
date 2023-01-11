""" 
Created on : 14/10/22 9:54 AM
@author : ds  
"""

data = [
    ["O", "X", "X"],
    ["X", "X", "X"],
    ["O", "#", "X"]
]


def tic_tac_toe(inputs):
    rotated = list(zip(*inputs[::-1]))
    diag1 = [inputs[0][0], inputs[1][1], inputs[2][2]]
    diag2 = [inputs[0][2], inputs[1][1], inputs[2][0]]
    if all(i == "X" for i in inputs[0]) or all(i == "X" for i in inputs[1]) or all(i == "X" for i in inputs[2]) or \
            all(i == "X" for i in rotated[0]) or all(i == "X" for i in rotated[1]) or all(i == "X" for i in rotated[2])\
            or all(i == "X" for i in diag1) or all(i == "X" for i in diag2):
        return "Player 1 wins"
    elif all(i == "O" for i in inputs[0]) or all(i == "O" for i in inputs[1]) or all(i == "O" for i in inputs[2]) or \
            all(i == "O" for i in rotated[0]) or all(i == "O" for i in rotated[1]) or all(i == "O" for i in rotated[2])\
            or all(i == "O" for i in diag1) or all(i == "O" for i in diag2):
        return "Player 2 wins"
    else:
        return "It's a Tie"


print(tic_tac_toe(data))
