while True:
    try:
        int_one = int(input("Enter integer one: "))
        int_two = int(input("Enter a second integer: "))
        break
    
    except ValueError:
        print("Value must be an integer")

print(f"The quotient of {int_one} and {int_two} is {int_one // int_two} with a remainder of {int_one % int_two}")