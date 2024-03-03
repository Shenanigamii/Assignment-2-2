# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here

# gets the current callendar year
import datetime 
currentYear = datetime.datetime.now().year
# gets the users birth year from user input
birthYear = input("To see how old you will be in the year 2050, enter the year you were born: ")
birthYear = int(birthYear)
# establishes current age
myCurrentAge = currentYear - birthYear
# creates users future age in 2050
myNewAge = myCurrentAge + (2050 - currentYear)
# voila
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")