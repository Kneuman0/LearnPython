'''
Created on Nov 22, 2016

@author: Karottop
'''
import random
from chapter11.lab7.Board import GameBoard

class Player:
    
    def __init__(self, gameBoard):
        self.board = gameBoard
    
    def getPlayerMove(self, mc):
        #print("getPlayerMove")
        playerMove = ""
        player = "X"
        cellOK = False
        over = False
        row = 0
        col = 0
    
        while cellOK == False and mc<=9:
            playerMove = input("Human: Enter your move (row col): ")
            #parse out row and column
            row = int(playerMove[0])
            col = int(playerMove[1])
            if self.board.cellTaken(row, col) == True:
                cellOK = False  # cell is full
            else:
                # put an X at the coordinates entered by the user
                self.board.board[row][col] = player
                cellOK = True
    
        #Did I win?
        if (mc >= 5):
            if self.board.checkForWinner("X") == True:
                print("X wins - Humans Rule!")
                self.board.toString()
                over = True
            
                
        return over
    
    def getComputerMove(self, mc):
        #print("getComputerMove")
        player = "O"
        cellOK = False
        over = False
        randomRow = 0
        randomCol = 0
    
        while cellOK == False and mc<=9:
            randomRow = random.randint(0,2)
            randomCol = random.randint(0,2)
            if (self.board.cellTaken(randomRow, randomCol)==True):
                cellOK = False  # cell is full
            else:
                # put an O at the coordinates entered by the user
                self.board.board[randomRow][randomCol] = player
                cellOK = True
    
        #Did I win?
        if (mc >= 5):
            if (self.board.checkForWinner("O") == True):
                print("O wins - Computers Rule!")
                self.board.toString()
                over = True
                
        return over