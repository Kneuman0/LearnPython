'''
Created on Sep 22, 2016

@author: Karottop
'''
print("Lab 3. Vowels Problem. Kyle Neuman")
phrase = input("Please enter a phrase\n").lower()

vowels = "aeiou"

# incrementer
totalVowels = 0

for char in phrase:
    if char in vowels:
        totalVowels += 1

        
print("There are {} vowels in that phrase".format(totalVowels))
                            