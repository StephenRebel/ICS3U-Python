# Importing the math library
import math
while True:
    try: 
        radius = float(input("Please enter a radius: ")) # Asks user for the desired radius13.5
        break
    except ValueError:
        print("Value must be of type float or int")

"""
This print statement uses f-strings to easily print strings and other numerical values
Calculations are included in the print statement as these values do not need to be used
again in the program, thus so not need to be stored in variables.
"""

print(f"The area is {round(math.pi*radius**2,1)} and the circumference is {round(2*math.pi*radius,1)}")