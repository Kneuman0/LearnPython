'''
Created on Oct 12, 2016

@author: Karottop
'''
def main():
    inputVal = int(input("Please enter a charge account to verify: "))
    if validateChargeAccount(inputVal):
        print("Account number ", inputVal, " is valid!")
    else:
        print("Account number ", inputVal, " is not valid!")
    
def readFileIntoList():
    buffer = None
    try:
        buffer = open("charge_accounts.txt", "r")
    except FileNotFoundError:
        print("Nope. Wrong file name")
    
    charges = []
    for line in buffer:
        charges.append(int(line))
       
    return charges 

def validateChargeAccount(inputValue):
    chargeAccounts = readFileIntoList()
    try:
        chargeAccounts.index(inputValue)
    except ValueError:
        return False
    
    return True;
main()