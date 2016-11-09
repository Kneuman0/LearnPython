'''
Created on Nov 8, 2016

@author: Karottop
'''
CODE = {"A":"B", "B":"C", "C":"D", "D":"E", "E":"F", "F":"G", "G":"H", "H":"I", \
        "I":"J", "J":"K", "K":"L", "L":"M", "M":"N", "N":"O", "O":"P", "P":"Q", \
        "Q":"R", "R":"S", "S":"T", "T":"U", "U":"V", "V":"W", "W":"X", "X":"Y", \
        "Y":"Z", "Z":"^", "a":"b", "b":"c", "c":"d", "d":"e", "e":"f", "f":"g", \
        "g":"h", "h":"i", "i":"j", "j":"k", "k":"l", "l":"m", "m":"n", "n":"o", \
        "o":"p", "p":"q", "q":"r", "r":"s", "s":"t", "t":"u", "u":"v", "v":"w", \
        "w":"x", "x":"y", "y":"z", "z":"%"}

def main():
    para = readInString()
    encrypted = encrypt(para)
    printToFile(encrypted)
    
    
    
    
    
def readInString():
    buffer = open("uncrypt.txt")
    para = ""
    for line in buffer:
        para += "{}".format(line)
    
    return para

def encrypt(para):
    encryt = ""
    for index in range(len(para)):
        if para[index] in CODE:
            encryt += CODE[para[index]]
        else:
            encryt += para[index]
    
    return encryt

def printToFile(paragraph):
    buffer = open("encrypted.txt", "w")
    print(paragraph, file = buffer)
    
main()
            
        