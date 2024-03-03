# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here
  # Gets the current calendar year
# Other Viable Code in lines 9 and 10 
# Remove line 11 if using lines 9 and 10 to keep current after the year 2024
      #import datetime 
      #currentYear = datetime.datetime.now().year
currentYear = 2024
  # Gets the users birth year from user input
birthYear = input("To see how old you will be in the year 2050, enter the year you were born: ")
birthYear = int(birthYear)
  # Establishes current age
myCurrentAge = currentYear - birthYear
  # Creates users future age in 2050
myNewAge = myCurrentAge + (2050 - currentYear)
  # Voila
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in 2050.")