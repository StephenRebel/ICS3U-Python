"""
Stephen Rebel: Number guessing game

This program is a small game for my ICS3U course where a user will be given the choice of
entering their own custom value set or playing with a pre generated set with slight randomization.
This game will prompt a user to enter a number and will give hints if they are too high or too low.
The game will end when the user has guessed the correct number that will be randomly selected
each playthrough. The user has the option to play again or to quit.
"""

# importing the random library so i can use random numbers in my program
import random

# This is a function that will prompt the user to guess, and then return the value
def guess(upper_bound, lower_bound):
    while True:
        # Bullet proofing is used to assure valid inputs
        try:
            # User prompt to imput an integer
            user_guess = int(input("Guess a positive integer: "))
            if user_guess <= upper_bound and user_guess >= lower_bound:
                break
            # Error or range value error messages
            else:
                print(f"Sorry, that value is not within the range of {lower_bound} and {upper_bound}")
        except ValueError:
            print("Sorry, that is not an acceptable value, must be an integer")
    return user_guess

# Determines wheter the user would like to reset the scores or not, contains bullet proofing
while True:
    file_clear = input("Would you like to reset the scores from your last playthough? If this is your first playthrough please enter 'first':  ")
    if file_clear == "yes" or file_clear == "no" or file_clear == "first":
        break
    else:
        print("Sorry, you must input either 'yes' or 'no', or 'first'")

# Will determin if the file will be reset or not
if file_clear == "yes" or file_clear == "first":
    # Initializes and resets the file that contains the score values and names
    f = open("Scores.txt", "w")
    f.write("Scores:")
    f.close()
    # High score file starts here
    g = open("Highscores.txt", "w")
    g.close()
    if file_clear == "yes":
        print("Scores have been reset")
    else:
      print("File has been created")
else:
    # Will instead do nothing to the file and leave it as it is, or if the file does not exist
    # nothing will happen
    print("Your new scores will be added to the existing ones")

# Initializing the main game loop
while True:

    h_scores =[]
    g = open("Highscores.txt", "r")
    for line in g:
        h_scores.append(int(line))
    g.close()

    # Initializing the counter variable and resetting if the user wishes to play again
    num_guesses = 0

    # Determins which version of the game the user wants to play
    while True:
        # Bullet proofing to only accept the desired inputs
        game_type = input("Would you like to play a 'custom' number set or a 'computer' generated set? ")
        if game_type == "custom" or game_type == "computer":
            break
        else:
            print("You must enter the words 'custom' or 'computer' as a response")
            
    # If statement sets the ranges for the game based on the user input from the previous question
    if game_type == "custom":
        # Does a bullet proofing check to make sure the user inputs a proper value, using try except and ifs
        while True:
            try:
                lower_bound = int(input("Please enter a positive integer for the lower bound: "))
                upper_bound = int(input("Please enter a positive integer for the upper bound: "))
                if lower_bound >= 0 and upper_bound >= 0 and lower_bound < upper_bound:
                    break
                elif lower_bound < 0 or upper_bound <0:
                    print("The range values must be greater than 0")
                else:
                    print("The lower bound cannot be greater than the upper bound")
            except ValueError:
                print("Invalid input, you must input an integer")
    else:
        lower_bound = random.randint(1, 20)
        upper_bound = random.randint(100, 150)
    
    # Sets the target number to a random integer in the range chosen
    target_num = random.randint(lower_bound, upper_bound)
    
    # Tell use the range of numbers so their guesses dont have to be completely random
    print(f"The range of values it {lower_bound} to {upper_bound}")
    
    # Initializing the game loop
    while True:
        """
         Sets the user_num = to the result of calling the guess function,
         then checks if the guess is higher lower or equal to the target number.
         The program will give hints or exit the loop depending on the guess
        """
        user_num = guess(upper_bound, lower_bound)
        num_guesses += 1
        if user_num == target_num:
            break
        elif user_num > target_num:
            print("Sorry, your guess was too high")
        else:
            print("Sorry, your guess was too low")
    
    # The user has won the game and exitted the game loop, these prints tell them about their win
    print(f"Congratulations, your guess the correct number, {target_num}")
    print(f"You took {num_guesses} guesses to guess the correct number")

    # Starts the loop for bullet proofing and asking if the user wants to save their score
    while True:
        take_score = input("Would you like to save your score? ")
        if take_score == "yes" or take_score == "no":
            break
        else:
            print("Sorry, you msut input 'yes' or 'no'")
    
    # Determines if the user wanted to save their score or not and uses file handling to save it
    if take_score == "yes":
        # Handles asking for a valid player name and bullet proofing
        while True:
            player_name = input("Please enter your username: ")
            if all(char.isalpha() or char.isspace() for char in player_name):
                print(f"Thank you {player_name}")
                break
            else:
                print("Sorry, your username can only contain letters and spaces")
        # File handling, the file will be oppened to append, a new line will be started
        # and the players name and their score will be added
        f = open("Scores.txt","a")
        f.write("\n")
        f.write(player_name + " took " + str(num_guesses) + " guesses")
        f.close()

        # file handling that reinputs the highscores from a sorted list
        h_scores.append(num_guesses)
        h_scores.sort()
        g = open("Highscores.txt", "w")
        for x in h_scores:
            g.write(str(x) + "\n")
        g.close()

    # Asks the user if they want to view the score sheet, bullet proofed
    while True:
        score_intent = input("Would you like to see the scores? 'yes' or 'no': ")
        if score_intent == "yes" or score_intent == "no":
            break
        else:
            print("Sorry, you must input either 'yes' or 'no'")

    # Based on the response will open and display the file to the terminal, or ignore if not wanted
    if score_intent == "yes":
        f = open("Scores.txt", "r")
        print(f.read())
        f.close()
        print("\n")
        print("Highscores: ")
        g = open("Highscores.txt", "r")
        print(g.read())
        g.close()

    # Ask the player if they wish to play again, then using the if decides
    # what to do based on the input
    while True:
        # Bullet proofing to only accept the desired inputs
        play_again = input("Would you like to play again? 'yes' or 'no': ")
        if play_again == "yes" or play_again == "no":
            break
        else:
            print("Invalid input, you must input the words, 'yes' or 'no'")

    if play_again == "yes":
        print("Alright, the game is restarting")
    else:
        break

# Final statement confirming the player has exitted the program, and thanks them for playing
print("Thanks for playing!")