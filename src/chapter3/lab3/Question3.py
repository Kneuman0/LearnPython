'''
Created on Sep 22, 2016

@author: Karottop
'''
import string
print("Lab 3. Password Problem. Kyle Neuman")

password = input("Please enter a password that has is at least 8 characters long\n" \
    "It should contain 1 uppercase,\n1 lowercase,\n1 number and\n1 special character\n")

specialCharPresent = False
for specialChar in string.punctuation:
    if specialChar in password:
        specialCharPresent = True
        break
    
capitalLetter = False
for capital in string.ascii_uppercase:
    if capital in password:
        capitalLetter = True
        break
    
lowerCase = False
for lowercase in string.ascii_lowercase:
    if lowercase in password:
        lowerCase = True
        break

numberPresent = False
for number in string.digits:
    if number in password:
        numberPresent = True
        break
    
passwordOK = specialCharPresent and capitalLetter and lowerCase and numberPresent and len(password) > 7

while not passwordOK:

    password = input("Invalid password, please try again")
    specialCharPresent = False
    for specialChar in string.punctuation:
        if specialChar in password:
            specialCharPresent = True
            break
    
    capitalLetter = False
    for capital in string.ascii_uppercase:
        if capital in password:
            capitalLetter = True
            break
    
    lowerCase = False
    for lowercase in string.ascii_lowercase:
        if lowercase in password:
            lowerCase = True
            break

    numberPresent = False
    for number in string.digits:
        if number in password:
            numberPresent = True
            break
    
    passwordOK = specialCharPresent and capitalLetter and lowerCase and numberPresent and len(password) > 7
    
secondPassword = input("Please enter your password again")

if secondPassword == password:
    print("Password set!")
else:
    print("Passwords do not match!\nProgram finished")
    raise SystemExit