'''
Created on Sep 22, 2016

@author: Karottop
'''
print("Lab 3. Vowels Problem. Kyle Neuman")
phrase = input("Please enter a phrase\n").lower()

vowels = "aeiou"

# incrementer
totalVowels = 0

# loop through all vowels
for vowel in vowels:
    
    #replace temp with phrase for each new vowel
    temp = phrase
    
    # if there is a vowel, loop until you cannot find anymore
    while temp.find(vowel) != -1:
        index = temp.find(vowel)
        if(index != -1):
            #increment each vowel found
            totalVowels += 1
            # get substring 1 char ahead of index of last vowel if not last char in string
            if index + 1 < len(temp):
                temp = temp[index + 1:]
        
print("There are {} vowels in that phrase".format(totalVowels))
                            