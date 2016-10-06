'''
Created on Oct 6, 2016

@author: Karottop
'''
import random

def main():
    fileName = input("Please enter a file name that you'd like to write to: ")
    amount = int(input("Please enter the number of times you'd like to print a number to the file: "))
    writeFile(fileName, amount)
    
    
def openFile(fileName):
    return open(fileName, "w")
    
def writeFile(fileName, amountOfNumbers):
    buffer = openFile(fileName)
    
    for index in range(amountOfNumbers):
        print(random.randint(1,500), file= buffer)
        
    close(buffer)
    
def close(buffer):
    buffer.close()
    print("File printed")
    
main()