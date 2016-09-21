'''
Created on Sep 20, 2016

@author: Karottop
'''

print("Lab 2. Grades Problem. Kyle Neuman")

numberOfStudents = int(input("How many students do you want to average grades for?\n"))

for student in range(numberOfStudents):
    print("What is the name of student ", student + 1, "?\n")
    studentName = input()
    
    print("Enter a grade for ", studentName, " that is >= 0 and <= 100\n To escape enter -1\n")
    gradeForStudent = float(input())
    
    gradeTotal = 0
    numberOfGrades = 0
    while 0 <= gradeForStudent <= 100:
        numberOfGrades += 1
        gradeTotal += gradeForStudent
        print("Enter a grade for ", studentName, " that is >= 0 and <= 100\n To escape enter -1\n")
        gradeForStudent =  float(input())
    
    average = 0;
    if numberOfGrades != 0:
        average = float(gradeTotal) / float(numberOfGrades)
        
    print("Grade for ", studentName, " is: ", average)