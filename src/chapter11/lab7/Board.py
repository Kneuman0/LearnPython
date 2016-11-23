'''
Created on Nov 22, 2016

@author: Karottop
'''
class GameBoard:
    def __init__(self, rows, columns):
        self._board = self.initalizeGameBoard([], rows, columns)
    
    def initalizeGameBoard(self, listBoard, rows, cols):
        for r in range(rows):
            listBoard.append([])  # Append rows.
            for c in range(cols):
                listBoard[r].append("-")  #Append columns.
        return listBoard
    
    def cellTaken(self, r, c):
        return self.board[r][c] == "X" or self.board[r][c] == "O"
    
    def checkForWinner(self, player):
        winner = False
    
        #Row 0
        if (self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player):
            winner=True
        #Row 1
        if (self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player):
            winner=True
        #Row 2
        if (self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player):
            winner=True
    
        #Column 0
        if (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player):
            winner=True
        #Column 1
        if (self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player):
            winner=True
        #Column 2
        if (self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player):
            winner=True
    
        #Diagonal \
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
            winner=True        
    
        #Diagonal /
        if (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            winner=True
    
        return winner
    
    def toString(self):
        for row in self.board:
            # Loop over columns.
            for column in row:
                print(column, " ", end="")
            print(end="\n")
    
    @property
    def board(self):
        return self._board
