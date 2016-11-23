'''
Created on Nov 22, 2016

@author: Karottop
'''
import Player
import Board
def main():
    # Inialize gameboard
    gameBoard = Board.GameBoard(3,3)
    # Initalze human player
    human = Player.Player(gameBoard)
    # inialize computer player
    computer = Player.Player(gameBoard)
    moveCount = 0
    # display gameboard
    gameBoard.toString()
    # Set the moves
    moveCount, gameOver = setMoves(human, computer, moveCount)
    
    # Loop until wither there are no more slots or 
    while checkMoveCount(moveCount, gameBoard, gameOver) and not gameOver:
        gameBoard.toString()
        moveCount, gameOver = setMoves(human, computer, moveCount)
    
def setMoves(human, computer, moveCount):
    moveCount += 1
    if human.getPlayerMove(moveCount):
        return moveCount, True
    
    moveCount += 1
    if computer.getComputerMove(moveCount):
        return moveCount, True
    return moveCount, False

def checkMoveCount(moveCount, board, gameOver):
    if moveCount <= 8:
        return True
    elif moveCount > 8 and not gameOver:
        print("It's a draw!")
        print(board.toString())
        return False
    else:
        return False

main()
    
