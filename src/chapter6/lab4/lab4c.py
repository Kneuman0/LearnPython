'''
Created on Oct 6, 2016

@author: Karottop
'''
def main():
    fileName = input("Please enter a file name to be parsed")
    password, index, totalWordCount = findPassword(fileName)
    
    print("There are {} words in the file.\n" \
          "The password is {}, found at the index {}".format(totalWordCount, password, index))

def getBuffer(fileName):
    buffer = None
    while buffer == None:
        try:
            buffer = open(fileName, "r")
        except:
            fileName = input("File does not exist. Try again.\nPlease enter a file name: ")
    
    return buffer

def findPassword(fileName):
    buffer = getBuffer(fileName)
    counter = 0
    password = None
    passwordIndex = 0
    
    for line in buffer:
        tokens = line.split(" ")
        
        for index in range(len(tokens)):
            counter += 1
            
            if tokens[index] == "password":
                password = tokens[index + 1]
                passwordIndex = counter
    
    buffer.close()
    return password, passwordIndex, counter
    
        
main()            
            
            
            
            
            