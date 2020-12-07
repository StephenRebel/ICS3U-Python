while True:
    try:
        mark = int(input("Please enter a mark between 0-100: "))
        if mark >= 0 and mark <= 100:
            print("Thank you")
            break
        else:
            print("Value must be between 0 and 100")

    except ValueError:
        print("Invalid mark, must be an integer")