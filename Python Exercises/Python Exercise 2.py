# Importing the math library
import math
radius = float(input("Please enter a radius: ")) # Asks user for the desired radius

# These expressions perform the calculations for area and circumference of a circle
area = math.pi*radius**2
circumference = 2*math.pi*radius

#This print statement uses f-strings to easily print and strings and other numerical values
print(f"The area is {round(area,1)} and the circumference is {round(circumference,1)}")