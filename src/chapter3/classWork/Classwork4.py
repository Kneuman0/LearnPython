'''
Created on Sep 21, 2016

@author: Karottop
'''

# Question 1
print("Classwork #4. Problem 1. Kyle Neuman")
phrase = input("Please enter a phrase\n")
# a
print("First letter: {}".format(phrase[0]))
# b
print("Last Letter: {}".format(phrase[-1]))
# c
print("Last letter: {}".format(phrase[len(phrase)-1]))
# d
print("First phrase in phrase: {}".format(phrase.split(' ')[0]))

# Question 2
print("\n\n--------------------------------")
print("Classwork #4. Problem 2. Kyle Neuman")
phrase = "wordproblem"
print(phrase[:4])
print(phrase[4:])

# Question 3
print("\n\n--------------------------------")
print("Classwork #4. Problem 27. Kyle Neuman")

phrase = input("Please enter a phrase")

print(phrase[::-1])

# Question 4
print("\n\n--------------------------------")
print("Classwork #4. Problem 28. Kyle Neuman")
word = "Luonohki naw fsfterkidnsg"
print(word[::2])