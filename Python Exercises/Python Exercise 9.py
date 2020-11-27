int_list = list(input("Enter an integer: "))

int_list = list(map(int, int_list))
print(f"There are {len(int_list)} digits in this integer, the sum of the digits is: {sum(int_list)}")

