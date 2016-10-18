'''
Created on Oct 18, 2016

@author: Karottop
'''
import random
def main():
    player1 = getListOfRandomInts(6, 1, 5)
    player2 = getListOfRandomInts(6, 1, 5)
    player1Sum = sum(player1)
    player2Sum = sum(player2)
    
    print("Player1 has: ", player1)
    print("Player2 has: ", player2)
    print("Player 1 total: ", player1Sum)
    print("Player 2 total: ", player2Sum)
    
    if player1Sum > player2Sum:
        print("Player 1 wins!")
    elif player1Sum < player2Sum:
        print("Player 2 wins!")
    else:
        print("Its a tie!")
    
    
    
def getListOfRandomInts(size, lower, upper):
    listOfInts = []
    for index in range(size):
        listOfInts.append(random.randint(lower, upper))
    return listOfInts
main()