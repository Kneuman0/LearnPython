'''
Created on Oct 12, 2016

@author: Karottop
'''
print("Lab5a. Number Analysis. Kyle Neuman")

def main():
    listOfNumber = getUserList()
    
    sortedList = sorted(listOfNumber)
    sortedListDec = list(reversed(sortedList))
    print ("Sorted List ascending: ", sortedList)
    print("Sorted list descending: ", sortedListDec)
    print("Smallest number: ", sortedList[0])
    print("largest number: ", sortedList[len(sortedList) - 1])
    print("Total of numbers in the list: ", getListTotal(listOfNumber))
    print("Average of number in the list: ", getAverage(listOfNumber))
 
def getUserList():
    listOfNumbers = []
    for index in range(10):
        number = None
        while(number == None):
            try:
                number = int(input("Please enter number {} of 10: ".format(index + 1)))
            except ValueError:
                print("Not a number! Please try again")
        
        listOfNumbers.append(number)
    
    return listOfNumbers

def getListTotal(listVar):
    total = 0
    for element in listVar:
        total += element
    
    return total

def getAverage(listVar):
    total = getListTotal(listVar)
    return float(total) / float(len(listVar))

main()