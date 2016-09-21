'''
Created on Sep 21, 2016

@author: Karottop
'''
print("Lab 2. Question Problem. Kyle Neuman")

rate = int(input("Please enter a rate in miles per hour"))
time = int(input("Please enter the amount of time the vehicle travels at that rate"))

while rate < 0:
    print("You have entered an invalid rate. Please enter a rate above 0")
    rate = int(input("Please enter a rate in miles per hour"))
    
while time < 0:
    print("You have entered an invalid time. Please enter a time above 0")
    time = int(input("Please enter the amount of time the vehicle travels at that rate"))
    
for hour in range(time):
    print("Hour: ", hour + 1, "Distance: ", rate * (hour + 1))