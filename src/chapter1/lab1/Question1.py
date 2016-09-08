import math

number1 = input("Please enter your first number\n")
number2 = input("Please enter your second number")
number1Float = float(number1)
number2Float = float(number2)

print("sum: ", (number1Float + number2Float))
print("Difference: ", (number1Float - number2Float))
print("Product: ", (number1Float * number2Float))
print("Quotient: ", (number1Float / number2Float))
print("Remainder: ", (number1Float % number2Float))
print("Power Using **: ", (number1Float ** number2Float))
print("Power Using pow(): ", math.pow(number1Float, number2Float))