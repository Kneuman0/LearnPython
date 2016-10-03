'''
Created on Oct 3, 2016

@author: Karottop
'''

import math

print("CW05a. Math Formulas. Kyle Neuman")

print("Please make a selection:\n1. Square\n2. Circle\n3. Rectangle\n4. Triangle")

def main():
    choice = int(input("Please enter one of the choices above: "))
    
    if choice == 1:
        square()
    elif choice == 2:
        circle()
    elif choice == 3:
        rectangle()
    elif choice == 4:
        triangle()
    else:
        print("You have not entered a valid choice")

def triangle():
    a = float(input("TRIANGLE/nPlease enter the length of the first side: "))
    b = float(input("Please enter the length of the second side: "))
    c = float(input("Please enter the length of the third side: "))
    C = math.acos((b**2 + a**2 - c**2)/(2.0*a*b))
    height = b * math.sin(C)
    perimeter = a + b + c 
    area = .5 * a * height
    print("The permimeter is: {}/nThe Area is: {}".format(perimeter, area))

def square():
    side = float(input("SQUARE/nPlease enter the length of a side: "))
    print("The perimeter is: {}/n The area is: {}".format(4 * side, side**2))
    
def rectangle():
    sideA = float(input("Please enter the length of one of the sides"))
    sideB = float(input("Please enter the length of the other side"))
    print("The perimeter is: {}/n The area is: {}".format(2 * sideA + 2 * sideB, sideA * sideB))
    
def circle():
    radius = float(input("Circle/nPlease a radius: "))
    print("The perimeter is: {}/n The area is: {}".format(2 * math.pi * radius, math.pi * (radius**2)))
    
main()