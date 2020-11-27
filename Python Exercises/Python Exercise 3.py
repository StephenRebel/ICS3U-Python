while True:
    mark = int(input("Please enter a mark between 1-100: "))
    if mark >= 0 and mark <= 100:
        print("Thank you")
        break
    else:
        print("Invalid mark")