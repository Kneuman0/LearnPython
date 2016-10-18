'''
Created on Oct 18, 2016

@author: Karottop
'''
import random

def main():
    names = ["Kesha", "Rick", "Jeff", "Robert", \
             "Bobby", "Jethrow", "Bilbert", "Kennedy", "Sarah", "George"]
    
    winner, index = getRandomIndexValue(names)
    print("The contestants are {}".format(names))
    print("The winning # is: {}\nThe Winner is: {}".format(index + 1, winner))
    
def getRandomIndexValue(array):
    size = len(array)
    randomIndex = random.randint(0, (size - 1))
    return array[randomIndex], randomIndex

main()