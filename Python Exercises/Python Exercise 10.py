import random
play_again = "yes"

while play_again == "yes":
  roll_two = 0
  count = 0
  roll_one = random.randint(1,6)
  print("Your first roll and point value is: " + str(roll_one))
  while roll_two != roll_one:
    roll_two = random.randint(1,6)
    count += 1
    print("Next role is: " + str(roll_two))
  print(f"It took you {count} roles to get your point again.")
  while True:
    play_again = input("Do you want to play again? ('yes','no'): ")
    if play_again == "yes" or play_again == "no":
      break
    else:
      print("Sorry you must input either 'yes' or 'no'")
  print("\n\r")