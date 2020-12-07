def correct_input():
  while True:
    try:
      user_num = float(input("Please enter a real number: "))
      return user_num
    except ValueError:
      print("That is not an acceptable value for a real number")

print(f"You entered the real number: {correct_input()}")