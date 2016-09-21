'''
Created on Sep 20, 2016

@author: Karottop
'''
print("Lab 2. Change Problem. Kyle Neuman")
quarters = int(input("Please enter the number of quarters:\n"))
dimes = int(input("Please enter the number of dimes:\n"))
nickles = int(input("Please enter the number of nickles:\n"))
pennies = int(input("Please enter the number of pennies:\n"))

changeTotal = (.25 * quarters) + (.1 * dimes) + (.05 * nickles) + (.01 * pennies)

if changeTotal > 1.00:
    print("You have more than a dollar in change: ", changeTotal)
elif changeTotal < 1.00:
    print("You have less than a dollar in change ", changeTotal)
else:
    print("You exactly a dollar in change! Hurray!")
    