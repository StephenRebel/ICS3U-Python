# Imports the time library so I can use delays
import time

# Imports only the system and name from the os library
from os import system, name

# Importing a grpahing library
import matplotlib.pyplot as plt 

# Function that will determin the type of os the user is running
# and will clear the sceen based on the os found
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# A function that will get user input for the variables and return them
def user_var(func_type):
    # Bullet proofing to assure valid numbers are input
    while True:
        try:
            a = float(input("Please enter the value for a: "))
            b = float(input("Please enter the value for b: "))
            c = float(input("Please enter the value for c: "))
            if func_type == 1:
                if b == 0:
                    print("For a linear function b cannot = 0")
                else:
                    break
            elif func_type == 2:
                if a == 0:
                    print("For a quadratic function a cannot = 0")
                else:
                    break
        # Handles errors that would crash the program
        except ValueError:
            clear()
            print("You must enter a number for all values")
    # Prints the next line in the sequence that would be repeated no matter the function
    print(" {:10} X-Values: {:20} Y-Values: ".format("", ""))
    return a, b, c

# A procedure that will get user input for the variables of the advanced functions and output the table
def adv_user_var(adv_func_type):
    # Bullet proofing to assure valid numbers are input
    while True:
        try:
            a = float(input("Please enter the value for a: "))
            h = float(input("Please enter the value for h: "))
            k = float(input("Please enter the value for k: "))
            if adv_func_type == 3:
                while True:
                    b = float(input("Please enter the value for b from 0 - 10: "))
                    if b >=0 and b <= 10:
                        break
                    else:
                        print("b must be between 0 and 10")
            break
        # Handles errors that would crash the program
        except ValueError:
            print("You must enter a number for all values")
    # Prints the next line in the sequence that would be repeated no matter the function
    print(" {:10} X-Values: {:20} Y-Values: ".format("", ""))
    
    equa_x = h - 4
    while equa_x <= h + 4:
        # Based on which function is being used a decision for the y calculation is made
        if adv_func_type == 1:
            y = a*(equa_x - h)**3 + k
        elif adv_func_type == 2:
            y = a*abs(equa_x - h) + k
        else:
            y = a*b**(equa_x - h) + k
        print(" {:17.1f} {:31.2f} ".format(equa_x, y))
        equa_x += 1

    # Resets the x value for graphing calculations
    equa_x = h - 4
    # stores values for a graph in two lists
    while equa_x <= h + 4:
        if adv_func_type == 1:
            y_list.append(round(a*(equa_x - h)**3 + k, 3))
        elif adv_func_type == 2:
            y_list.append(round(a*abs(equa_x - h) + k, 3))
        else:  
            y_list.append(round(a*b**(equa_x - h) + k, 3))
        x_list.append(round(equa_x, 2))
        equa_x += 0.1
    # Creates the graph
    plt.plot(x_list, y_list)
    plt.xlabel('X - axis')
    plt.ylabel('Y - axis')
    if adv_func_type == 1:
        plt.title(f"Graph of the cubic function y = {a}(x - {h})^3 + {k}")
    elif adv_func_type == 2:
        plt.title(f"Graph of the absolute function y = {a}|x - {h}| + {k}")
    else:
        plt.title(f"Graph of the exponential function y = {a}x^(x - {h}) + {k}")
    plt.show()

# Beggining of main program loop
while True:
    # Initializing and resetting the graph value lists
    x_list = []
    y_list = []
    # Bullet proofing for user input of which type of function they would like
    while True:
        try:
            # Gets user input for type of function
            func_type = int(input("Please enter the typer of function you'd like. 1 for linear, 2 for quadratic, or 3 for more functions: "))
            if func_type ==1 or func_type == 2 or func_type == 3:
                break
            else:
                clear()
                print("Please enter either 1 for linear or 2 for quadratic or 3 fro the advanced functions: ")
        except ValueError:
            clear()
            print("You must enter a single integer")

    # Prints the table of values for a linear function using .format
    if func_type == 1:
        clear()
        print("For an equation in the form: 0 = ax + by + c")
        equa_vars = user_var(1)
        for x in range(-4, 5):
            y = -(equa_vars[0]*x + equa_vars[2]) / equa_vars[1]
            if y == 0:
                y = 0
            print(" {:17.1f} {:31.2f} ".format(x, y))
            x_list.append(round(x, 2))
            y_list.append(round(y, 3))
        # Creating line graph using previous values
        plt.plot(x_list, y_list)
        plt.xlabel('X - axis') 
        plt.ylabel('Y - axis')
        plt.title(f"Graph of the linear function y = -({equa_vars[0]}x + {equa_vars[2]}) / {equa_vars[1]}") 
        plt.show()

    # Prints the table of values for a quadratic function using . format
    elif func_type == 2:
        clear()
        print("For an equation in the form: y = ax^2 + bx + c")
        equa_vars = user_var(2)
        quad_vertex = -equa_vars[1]/(2*equa_vars[0])
        equa_x = quad_vertex - 4
        while equa_x <= quad_vertex + 4:
            y = equa_vars[0]*equa_x**2 + equa_vars[1]*equa_x + equa_vars[2]
            print(" {:17.1f} {:31.2f} ".format(equa_x, y))
            equa_x += 1
        # restes x value fro graph
        equa_x = quad_vertex - 4 
        while equa_x <= quad_vertex + 4:
            # create lists for graph values
            y_list.append(round(equa_vars[0]*equa_x**2 + equa_vars[1]*equa_x + equa_vars[2], 3))
            x_list.append(round(equa_x, 2))
            equa_x += 0.1
        # Opens the graph
        plt.plot(x_list, y_list)
        plt.xlabel('X - axis') 
        plt.ylabel('Y - axis')
        plt.title(f"Graph of the quadratic function y = {equa_vars[0]}x + {equa_vars[1]}x + {equa_vars[2]}") 
        plt.show()

    # gets user input for the 3 extra functions
    else:
        clear()
        print("You selected more functions")
        while True:
            try:
                adv_func_type = int(input("Please enter 1 for cubic, 2 for absolute value, or 3 for exponential: "))
                if adv_func_type == 1 or adv_func_type == 2 or adv_func_type == 3:
                    break
                else:
                    clear()
                    print("Please input either 1 for cubic, 2 for absolute, or 3 for exponential")
            except ValueError:
                print("You must enter an integer")

        # Calls for table function for cubic function
        if adv_func_type == 1:
            clear()
            print("For an equation in the form: y = a(x - h)^3 + k")
            adv_user_var(1)

        # Calls table procedure for absolute function
        elif adv_func_type == 2:
            clear()
            print("For an equation in the form: y = a|x - h| + k")
            adv_user_var(2)

        # Calls for the table procedure for exponential
        else:
            clear()
            print("For an equation in the form: y = a*b^(x - h) + k")
            adv_user_var(3)

    # Bullet proofing user input if they's like to run the program again
    while True:
        run_again = input("Would you like to input another function and set of values, Y/N: ")
        if run_again == "Y" or run_again == "N":
            break
        else:
            clear()
            print("Please enter 'Y' for yes and 'N' for no")

    # Restarts the program and adds delay so the user can read waht will happen
    if run_again == "Y":
        print("Ok, restarting")
        time.sleep(2)
        clear()
    else:
        break

#End of the program after exiting the loop, and thanks user for using the program
print("Thank you, have a good day")