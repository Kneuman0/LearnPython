'''
Created on Sep 16, 2016

@author: Karottop
'''

thing1 = 1
thing2 = 2
thing3 = 3
incrementer = 0

while incrementer < 5:
    
    print(incrementer + 1, "---------------------") 
    
    if thing1 > thing2:
        print("Something is wrong")
    else:
        print("Thing 1 is not greater than thing2")
        
    if thing1 > thing2:
        print("Something is really wrong")
    elif thing3 > thing2:
        print("Thing3 is greater than thing2")
    else:
        print("Something is wrong")
        
    incrementer += 1

things = ["stuff", "n", "things", "with", "widgets", "inside"]
    
for eachLetter in range(1,10):
    print(eachLetter)
    
for word in range(len(things)):
    print(word, ": ", things[word])  
    
if thing1 < thing2 or thing2 > thing3:
    print("All is good")  
    
   
        