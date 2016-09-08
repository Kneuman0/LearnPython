'''
Created on Sep 8, 2016

@author: Karottop
'''
# Problem 1 
number = int(input("cw02a. Time Problem. Kyle Neuman\n"  \
"Please enter a number between 1 and 86,400\n"))

# get remainder of seconds after hours have been divided out
hourReminder = int(number % 3600)
print("Hours: ", int(number/3600))

# get remainder of seconds after minutes have been divided out of hours remainder
minutesReminder = int(hourReminder % 60)
print("minutes: ", int(hourReminder/60))

# Whats left is seconds that do not make up a whole minute
print("Seconds: ", minutesReminder)
print("---------------------------")

# Problem 2
print("cw02b. Simple Interest. Kyle Neuman")
principle = int(input("Please enter your principle:\n"))
time = int(input("Please enter your term in years:\n"))
annualInterestRate = float(input("Please enter your annual interest rate:\n"))
print("Amount: ", principle)
print("time: ", time, " years")
print("Interest Rate: ", annualInterestRate * 100, "%")
interest = principle * time * annualInterestRate
print("Simple Interest: ", interest)
print("Total investment: ", principle + interest)
print("------------------------------")

# Problem 3
print("cw02c. Triangle Problem. Kyle Neuman")
a = int(input("Please enter side a of the triangle:\n"))
b = int(input("Please enter side b of the triangle:\n"))
hypotenuse = (a**2 + b**2)**(1/2)
print("The hypotenuse is: ", hypotenuse)







