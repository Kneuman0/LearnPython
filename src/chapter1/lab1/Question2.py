'''
Created on Sep 6, 2016

@author: Karottop
'''

# Constants
MILES_FROM_THE_SUN_START = 16637000000.0
VELOCITY_OF_TRAVEL_IN_MILES_PER_DAY = 38241 * 24.0
KILO_PER_MILE = 1.609344
Miles_PER_AU = 92955887.6
SPEED_OF_LIGHT_KILO_PER_HOUR = 299792458 * 3.6


numberOfDaysInt = float(input("How many days after 9/25/09? Please enter an integer\n"))

# Distance in miles
distanceInMiles = (numberOfDaysInt * VELOCITY_OF_TRAVEL_IN_MILES_PER_DAY) + MILES_FROM_THE_SUN_START
print("Distance in Miles: ", distanceInMiles)

# Distance in kilometers
distanceInKilo = distanceInMiles * KILO_PER_MILE
print("Distance in Kilometers: ", distanceInKilo)

# Distance in Astronomical Units (AU)
distanceInAU = distanceInMiles / Miles_PER_AU
print("Distance in AUs: ", distanceInAU)

# Time for Round Trip radio communication in hours 
# take inverse of speed of light (Raise to -1 power) and cancel distance with kilometers
timeInHoursRadioCom = ((SPEED_OF_LIGHT_KILO_PER_HOUR ** -1) * distanceInKilo) * 2
print("Time in hours for round trip radio transmission: ", timeInHoursRadioCom)

# Time For Round Trip radio comm in days
print("Time in days for round trip radio transmission: ", timeInHoursRadioCom / 24.0)

# Time for round trip radio comm in years
print("Time in years for round trip radio transmission: ", timeInHoursRadioCom / (24.0 * 365))