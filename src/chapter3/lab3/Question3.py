'''
Created on Sep 22, 2016

@author: Karottop
'''
import string
print("Lab 3. Password Problem. Kyle Neuman")

password = input("Please enter a password that has is at least 8 characters long\n" \
    "It should contain 1 uppercase,\n1 lowercase,\n1 number and\n1 special character\n")

def passwordCorrect(password):
    
    specialCharPresent = False
    capitalLetter = False
    lowerCase = False
    numberPresent = False
    for char in password:
        if char in string.ascii_lowercase:
            lowerCase =True
    
        if char in string.ascii_uppercase:
            capitalLetter = True
    
        if char in string.digits:
            numberPresent = True
        
        if char in string.punctuation:
            specialCharPresent = True
    
    if not specialCharPresent:
        print("Password must contain a special character")
        
    if not capitalLetter:
        print("Password must contain at least 1 capital letter")
    
    if not numberPresent:
        print("Password must contain at least 1 number")
        
    if len(password) < 8:
        print("Password must be at least 8 character long")
    
    return specialCharPresent and capitalLetter and lowerCase and numberPresent and len(password) >= 8


while not passwordCorrect(password):

    password = input("Invalid password, please try again\n")
    
    
    
secondPassword = input("Please enter your password again\n")

if secondPassword == password:
    print("Password set!")
else:
    print("Passwords do not match!\nProgram finished")
    raise SystemExit

