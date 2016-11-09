'''
Created on Nov 9, 2016

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
    print(decrypt(para))
    
    
def readInString():
    buffer = open("encrypted.txt")
    para = ""
    for line in buffer:
        para += line
    
    return para

def decrypt(para):
    unEncrypted = ""
    for index in range(len(para)):
        unEncrypted += getDecryptedChar(para[index])
    
    return unEncrypted
        
def getDecryptedChar(charValue):
    key = getDecryptDict()
    if charValue in key:
        return key[charValue]
    else:
        return charValue

def getDecryptDict():
    decript = {}
    for char, value in CODE.items():
        decript[value] = char;
    
    return decript
    
main()
        