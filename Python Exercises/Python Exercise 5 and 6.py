""""
mark = float(input("Enter your test mark: "))

#Version 1 of marks
print("Version 1")
if mark > 84 and mark <= 100:
    print("Level 4")
else:
    if mark >= 70 and mark < 85:
        print("Level 3")
    else:
        if mark >= 60 and mark < 70:
            print("Level 2")
        else:
            if mark >= 50 and mark < 60:
                print("Level 1")
            else:
                if mark >= 0 and mark < 50:
                    print("Level R")
                else:
                    print("Mark not in range")

print("Version 2")
#Version 2 of marks
if mark > 84 and mark <= 100:
    print("Level 4")
elif mark >= 70 and mark < 85:
    print("Level 3")
elif mark >= 60 and mark < 70:
    print("Level 2")
elif mark >= 50 and mark < 60:
    print("Level 1")
elif mark >= 0 and mark < 50:
    print("Level R")
else:
    print("Mark not in range")

print("Version 3")
#Version 3 of marks
if mark > 100 or mark < 0:
    print("Mark not in range")
elif mark > 84:
    print("Level 4")
elif mark >= 70:
    print("Level 3")
elif mark >= 60:
    print("Level 2")
elif mark >= 50:
    print("Level 1")
else:
    print("Level R")
"""
print("Thank you and goodbye")
"""
a. No, there are no differences in the versions of this program.
b. Version 3 is the most efficient version, aswell as being the easiest to read.
This is because of the compact and efficient use of statements and operators.
Unlike the other versions, ersion 3 terminates imediatly if an invalid grade is
inputted, which save sthe computer the trouble of checking any other if statements.
Version 3 also uses very effective logicical processes which demonstrate an
understanding of how python cheks if statements, they are in a good order which
demonstrate the programmer was aware that if the previous statement was false there
was no need to repeat that condition in the condition of the next line.
"""

"""
Excercise 6
"""
while True:
  price = float(input("What is the total price of your purchse: "))
  if price < 0:
    print("That is an invalid value")
  else:
    break

if price < 25:
  print("There are no savings available")
  print(f"The final cost is {price}")
elif price < 50:
  print("You can save 10%")
  print(f"The final cost is {price - (price*0.1)}")
elif price < 75:
  print("You can save 20%")
  print(f"The final cost is {price - (price*0.2)}")
elif price < 100:
  print("You can save 30%")
  print(f"The final cost is {price - (price*0.3)}")
else:
  print("You can save 40%")
  print(f"The final cost is {price - (price*0.4)}")