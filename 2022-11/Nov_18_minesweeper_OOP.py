""" 
Created on : 17/11/22 1:19 PM
@author : ds  
"""

# https://edabit.com/challenge/ub2KJNfsgjBMFJeqd

# This is a minesweeper board build using OOP.
# There are two classes-> Game and Cell

from random import randrange


class Game:
    def __init__(self, rows=14, columns=18, mines=40):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = []

        # initialise board
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns):
                self.board[i].append(Cell(i, j))
        # randomize mines

        while mines:
            mineRow, mineCol = randrange(0, rows), randrange(0, columns)
            if not self.board[mineRow][mineCol].mine:
                self.board[mineRow][mineCol].mine = True
                mines -= 1


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False

    def __repr__(self):
        return '*' if self.mine else '_'


game = Game(40, 56, 79)
print(game.rows)
print(game.columns)
print(game.mines)
print(game.board)
