import time

def user_var():
    while True:
        try:
            a = float(input("Please enter the value for a: "))
            b = float(input("Please enter the value for b: "))
            c = float(input("Please enter the value for c: "))
            break
        except ValueError:
            print("You must enter a number for all values")
    print(" {:10} X-Values: {:20} Y-Values: ".format("", ""))
    return a, b, c

while True:
    func_type = int(input("Please enter the typer of function you'd like. 1 for linear, 2 for quadratic: "))
    if func_type == 1:
        print("For an equation in the form: 0 = ax + by + c")
        equa_vars = user_var()
        for x in range(-4, 5):
            y = -(equa_vars[0]*x + equa_vars[2]) / equa_vars[1]
            print(" {:17.1f} {:31.2f} ".format(x, y))

    elif func_type == 2:
        print("For an equation in the form: y = ax^2 + bx + c")
        equa_vars = user_var()
        quad_vertex = (-1*equa_vars[1])/2*equa_vars[0]
        equa_x = quad_vertex - 4
        while equa_x >= quad_vertex - 4 and equa_x <= quad_vertex + 4:
            y = equa_vars[0]*equa_x**2 + equa_vars[1]*equa_x + equa_vars[2]
            print(" {:17.1f} {:31.2f} ".format(equa_x, y))
            equa_x += 1

    run_again = input("Would you like to input another function and set of values, Y/N: ")
    if run_again == "Y":
        print("Ok, restarting")
        time.sleep(3)
    else:
        break
print("Thank you, have a good day")      