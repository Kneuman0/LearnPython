'''
Created on Oct 18, 2016

@author: Karottop
'''
import time
MAX_VALUE = 999

def main():
    start = time.time()
    calculationResults = dict()
    for index in range(MAX_VALUE):
        answer = calculate(index)
        incrementSet(answer, calculationResults)
    print(calculationResults)    
    print("Execution Time: ", (time.time() - start) * 1000)    

def reverse(integer):
    intInStr = str(integer).zfill(len(str(MAX_VALUE)))[::-1]
    return int(intInStr)
    
def calculate(integer1):
    subtraction = abs(reverse(integer1) - integer1)
    return reverse(subtraction) + subtraction

def incrementSet(key, hashMap):
    if key in hashMap:
        hashMap[key] = hashMap[key] + 1;  
    else:
        hashMap[key] = 1;
        
main()