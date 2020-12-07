while True:
    try:
        int_list = list(map(int, list(input("Enter an integer: "))))
        break
    except ValueError:
        print("Input must be an integer")

print(f"There are {len(int_list)} digits in this integer, the sum of the digits is: {sum(int_list)}")

