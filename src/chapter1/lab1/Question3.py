'''
Created on Sep 6, 2016

@author: Karottop
'''
# constants
CURRENT_YEAR = 2016
BIRTHS_PER_YEAR = (3600 * 24 * 365) / 7.0
DEATHS_PER_YEAR = (3600 * 24 * 365) / 13.0
IMMIGRANTs_PER_YEAR = (3600 * 24 * 365) / 35.0
CURRENT_POPULATION = 307357870

year = int(input("What year would you like to calculate the volume for? Please enter an integer:\n"))

# how many years away and in what direction is the user asking to calculate for?
yearChange = year - CURRENT_YEAR
# How much has the population changed from the current year
populationChange = (yearChange * BIRTHS_PER_YEAR) - (yearChange * DEATHS_PER_YEAR) + (yearChange * IMMIGRANTs_PER_YEAR)
# This will work for dates before and after the current year
estimatedPopulation = int(CURRENT_POPULATION + populationChange)

print("The estimated population of ", year, "is: ", estimatedPopulation)