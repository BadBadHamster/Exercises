# Exercise 4 - Area of the field

# read input from user
length = float(input("Enter the lenght of the field in meters \n"))
width = float(input("Enter the width of the field in meters \n"))

# definition of units
acrespermeters = 100

# caclulations of area
area_cm = length * width
area_acr = length * width / acrespermeters

# results (rounded to 2 digits)
print("Field area in cubic meters equals", round(area_cm, 2), "m2")
print("Field area in acres equals", round(area_acr, 2), "acres")
