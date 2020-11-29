### Project #1: A Simple Game
"""
Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, 
your task is create a Connect 4 game in Python. Before you get started, please watch this video 
on the rules of Connect 4:
https://youtu.be/utXzIFEVPjA
Once you've got the rules down, your assignment should be fairly straightforward. You'll want to draw 
the board, and allow two players to take turns placing their pieces on the board 
(but as you learned above, they can only do so by choosing a column, not a row). 
The first player to get 4 across or diagonal should win!
Normally the pieces would be red and black, but you can use X and O instead.

Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a 
package like termcolor into your project. We're going to cover importing later in the course, 
but try and see if you can figure it out on your own. Or you might be able to find unicode characters 
to use instead, depending on what your system supports. Here's a hint: print(u'\u2B24')

"""

import numpy as ny
## numpy is used to create a matrix
from termcolor import colored, cprint

rowCounter = 6 # global variable to count the number of rows
columnCounter = 7 # global variable to count the number of columns


def createBoard():
    board = ny.zeros((rowCounter,columnCounter)) # creates a matrix of zeros with 6 lines and 7 columns
    return board

def locationMove(board, row, column, loc): # check the position in the board
    board[row][column] = loc

def isValidMove(board, column):
    return board[rowCounter-1][column] == 0

def nextRow(board, column):
    for i in range(rowCounter):
        if board[i][column] == 0:
            return i

def reverseBoard(board): # function to reverse the position of the matrix
    print(ny.flip(board, 0))

def win(board, loc):
    for c in range(columnCounter): # check the vertical places
        for r in range(rowCounter-3):
            if board[r][c] == loc and board[r+1][c] == loc and board[r+2][c] == loc and board[r+3][c] == loc:
                return True
    for c in range(columnCounter-3): # check the horizontal places
        for r in range(rowCounter):
            if board[r][c] == loc and board[r][c+1] == loc and board[r][c+2] == loc and board[r][c+3] == loc:
                return True
    for c in range(columnCounter-3): # check the diagonal places from right to left
        for r in range(rowCounter-3):
            if board[r][c] == loc and board[r+1][c+1] == loc and board[r+2][c+2] == loc and board[r+3][c+3] == loc:
                return True    
    for c in range(columnCounter-3): # check the diagonal places from left to right
        for r in range(3, rowCounter):
            if board[r][c] == loc and board[r-1][c+1] == loc and board[r-2][c+2] == loc and board[r-3][c+3] == loc:
                return True    


board = createBoard() # variable to the board
reverseBoard(board)
endGame = False # game still in progress
turn = 0 

while not endGame:
    # Player 1 move:
    if turn == 0:
        columnMove = int(input(colored("Player 1, please enter the column (from 0 to 6):\n", "blue", "on_grey"))) 
        if isValidMove(board, columnMove):
            row = nextRow(board, columnMove)
            locationMove(board, row, columnMove, 1)
            if win(board, 1): # checks the winner function
                cprint('Player 1 is the winner!', 'green', attrs=['bold'])
                endGame = True
    # Player 2 move:
    else: 
        columnMove = int(input(colored("Player 2, please enter the column (from 0 to 6):\n", "yellow", "on_grey"))) 
        if isValidMove(board, columnMove):
            row = nextRow(board, columnMove)
            locationMove(board, row, columnMove, 2)
            if win(board, 2):# checks the winner function
                cprint('Player 2 is the winner!', 'green', attrs=['bold'])
                endGame = True
    reverseBoard(board)
    turn += 1 # counter to add 1
    turn = turn % 2 # zeros the counter
