'''
Created on Oct 25, 2016

@author: Karottop
'''
print("CW-07a. Kyle Neuman")
def main():
    classNumber = input("Please enter a class number to query")
    room, instructor, meetingTime = getClassInfo(classNumber)
    print("The room number is: {}\nThe instructor is: {}\nThe meeting time is: {}"\
          .format(room, instructor, meetingTime)) 
 
def getRoomNumberSet():
    return {"CIS-101" : "A212", "CIS-132" : "K207", "CIS-137" : "K305", \
            "CIS-139" : "C071", "CIS-232" : "K207"}
  
def getInstructorSet():
    return {"CIS-101" : "Chaney", "CIS-132" : "Franzese", "CIS-137" : "Warburton", \
             "CIS-139" : "Barlet", "CIS-232" : "Rusk"}
  
def getMeetingTimeSet():
    return {"CIS-101" : "9:00 am", "CIS-132" : "12:30 pm", "CIS-137" : "8:00 am", \
            "CIS-139" : "6:00 pm", "CIS-232" : "6:30 pm"}
 
def getClassInfo(key):
    if key in getRoomNumberSet() and key in getInstructorSet() and key in getMeetingTimeSet():
        return getRoomNumberSet()[key], getInstructorSet()[key], getMeetingTimeSet()[key]
    else:
        print(key, "is not a valid class name")
        raise SystemExit
main()