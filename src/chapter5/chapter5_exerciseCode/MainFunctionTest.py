'''
Created on Oct 2, 2016

@author: Karottop
'''

print("Outside of main method")
def main():
    print("Print inside main method")
    printSomeStuff()
    var1, var2, var3 = returnSomeThings()
    print(var1, var2)
    
def printSomeStuff():
    print ("Hey look right here! I'm in a regular method")
    

def returnSomeThings():
    return 4, "s", 7
    
main()