'''
Created on Nov 8, 2016

@author: Karottop
'''
def main():
    first, sec = loadsets()
    print("Words in both: ", listList(first.union(sec)), "\n")
    print("Words that appear in both: ", listList(wordsInBoth(first, sec)) + "\n")
    print("Words that appear in list1 but not list2: ", listList(wordsInOneListButNotOther(first, sec)),"\n")
    print("Words that appear in list2 but not list1: ", listList(wordsInOneListButNotOther(sec, first)), "\n")
    print("Words in both: ", listList(first.union(sec)), "\n")
          
    
def loadsets():
    buffer1 = open("one.txt")
    buffer2 = open("two.txt")
    one = set()
    two = set()
    for line in buffer1:
        one.update(line.split())
    
    for line in buffer2:
        two.update(line.split())
    
    return one, two

def listList(listName):
    listString = ""
    for word in listName:
        listString += "\n{}".format(word)
    
    return listString

def wordsInBoth(list1, list2):
    both = set()
    for word in list1:
        if word in list2:
            both.add(word)
    
    return both

def wordsInOneListButNotOther(inList, notInList):
    unique = set(inList)
    for word in inList:
        if word in notInList:
            unique.remove(word)
    
    return unique

main()