'''
Created on Oct 3, 2016

@author: Karottop
'''
print("CW05b. Shopping List. Kyle Neuman")

def main():
    print("Welcome to shopping list manager 5000")
    fileName = input("Please enter the file name including the extension: ")
    print("Would you like to add to the list or read the list?")
    choice = int(input("Type 1 to add or 2 to read the list: "))
    
    if choice == 1:
        writeDATA(fileName)
    elif choice == 2:
        readDATA(fileName)
    else:
        print("You did not make a proper choice. Goodbye!")
        
def readDATA(fileName):
    shoppingList = open(fileName, "r")
    
    itemNumber = 1
    for item in shoppingList:
        print(itemNumber, ". ", item.strip())
        itemNumber += 1
    
def writeDATA(fileName):
    item = input("Please enter the item you'd like to add")
    shoppingList = open(fileName, "a")
    print(item, file = shoppingList)
    print("Item added!")
    
main()