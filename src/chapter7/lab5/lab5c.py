'''
Created on Oct 12, 2016

@author: Karottop
'''
def main():
    inputVal = input("Please enter a team name: ")
    wins = countWins(inputVal);
    timeOrTimes = "times"
    if wins == 1:
        timeOrTimes = "time"
        
    elif wins > 1:
        print("The team {} won the world series {} {}".format(inputVal, wins, timeOrTimes))
    else:
        print("The team {} never won the world series".format(inputVal))
    
            
def readFileIntoList():
    buffer = None
    try:
        buffer = open("WorldSeriesWinners.txt", "r")
    except FileNotFoundError:
        print("Nope. Wrong file name")
        raise  SystemExit
    
    winners = []
    for line in buffer:
        win = str(line.strip())
        winners.append(win)
       
    return winners

def countWins(inputValue):
    
    return readFileIntoList().count(inputValue);

main()