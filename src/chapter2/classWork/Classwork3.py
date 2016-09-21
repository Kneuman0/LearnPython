'''
Created on Sep 21, 2016

@author: Karottop
'''

# Odd or even number
print("CW03a. Odd or Even. Kyle Neuman")

number = int(input("Please enter a number\n"))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    
# Water temperature
print("\n\n-------------------------------------")
print("CW03b. Water Temperature. Kyle Neuman")

fahrenheit = int(input("Please enter a temperature in fahrenheit\n"))

if fahrenheit < 32:
    print("Water will freeze at this temp")
elif fahrenheit > 212:
    print("Water will boil at this temp")
else:
    print("Water is liquid at this temp")
    
# sum numbers from 1 to 10 in a loop
print("\n\n--------------------------------------")
print("CW03c. Sum number 1 to 10. Kyle Neuman")

total = 0
for index in range(10):
    print(total, " + ", index + 1, " = ", total + (index + 1))
    total += index + 1
    

print("\n\n-----------------------------------")
print("CW04d. Sum a range of numbers. Kyle Neuman")

beginningRange = int(input("Please enter a number that marks the beginning of a range"))
endingRange = int(input("Please enter a number that marks the end of a range"))

total = 0
for index in range(beginningRange, endingRange + 1):
    total += index
    
print("The sum of the range is", total)
    
    
    
    
    
    
    
    