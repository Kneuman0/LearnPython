'''
Created on Sep 20, 2016

@author: Karottop
'''
print("Lab 2. Color Problem. Kyle Neuman")

color1 = input("Please enter your first color\n")
colorlBool = color1 != "yellow" and color1 != "red" and color1 != "blue"

while colorlBool:
    print("You have entered an invalid color\n")
    color1 = input("Please enter your first color\n")
    colorlBool = color1 != "yellow" and color1 != "red" and color1 != "blue"
    
color2 = input("Please enter your second color\n")
color2Bool = color2 != "yellow" and color2 != "red" and color2 != "blue"

while color2Bool:
    print("You have entered an invalid color\n")
    color2 = input("Please enter your second color\n")
    color2Bool = color2 != "yellow" and color2 != "red" and color2 != "blue"

if color1 == "yellow" and color2 == "blue" or color2 == "yellow" and color1 == "blue":
    print("Blue")
    
elif color1 == "yellow" and color2 == "red" or color2 == "yellow" and color1 == "red":
    print("Orange")

elif color1 == "blue" and color2 == "red" or color2 == "blue" and color1 == "red":
    print("Purple")

else:
    print("Error! You have entered an invalid color!\n")
    
    


# while(color1 != )