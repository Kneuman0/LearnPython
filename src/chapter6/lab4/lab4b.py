'''
Created on Oct 6, 2016

@author: Karottop
'''
def main():
    fileName = input("Please enter a file name that you'd like to read from: ")
    total, counter, average = readData(fileName)
    print("There are were {} random numbers in the file.\nThe "  \
    "total is: {}.\nThe average is: {}".format(counter, total, average))
    
def readData(fileName):
    buffer = openFile(fileName)
    
    total = 0
    counter = 0
    for randNum in buffer:
        total += int(randNum)
        counter += 1
    
    return total, counter, total/float(counter)
    
def openFile(fileName):
    try:
        return open(fileName, "r")
    except:
        print("Invalid file name")
        raise SystemExit
    
def closeFile(buffer):
    buffer.close()
    
    
main()