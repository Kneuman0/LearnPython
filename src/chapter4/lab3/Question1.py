'''
Created on Sep 22, 2016

@author: Karottop
'''
print("Lab 3. Sum of Digits Problem. Kyle Neuman")
numberSeq = input("Please enter a number sequence of integers without spaces\n")

total = 0;
for number in range(len(numberSeq)):
    total += int(numberSeq[number])
    
print("The sum is: {}".format(total))