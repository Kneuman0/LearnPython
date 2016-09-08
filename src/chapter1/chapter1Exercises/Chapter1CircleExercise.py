import math

radiusString = input("Enter a radius for the circle \n")
radiusInt = int(radiusString)

# area = radiusInt * radiusInt * math.pi
circumfrence = 2 * radiusInt * math.pi

area = radiusInt * radiusInt * math.pi
circumfrence = 2 * radiusInt * math.pi

print("The Area of the circle is:", area,     \
      "\nAnd the circumfrence is: ", circumfrence)