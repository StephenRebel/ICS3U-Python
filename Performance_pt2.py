"""
This is a program by Stephen Rebel that will perform some mathimatical operations based on the numbers
a user submits
"""

import math
#Custom exception
class ValueOutOfRange(Exception):
    pass

#Run to get user input for their number
def user_input(menu_input):
    while True:
        try:
            user_num = int(input("\nPlease enter a number from 0 999999999: "))
            if menu_input == 3 and (user_num < 1 or user_num > 999999999):
                raise ValueOutOfRange
            if menu_input == 7 and (user_num < 0 or user_num > 999):
                raise ValueOutOfRange
            elif user_num < 0 or user_num > 999999999:
                raise ValueOutOfRange
            else:
                return user_num

        except ValueOutOfRange:
            if menu_input == 3:
                print("Sorry, to prime factor the value must be greater than 0")
            elif menu_input == 7:
                print("Sorry the value cannot be that high or below 0, please try between 0 and 999")

        except ValueError:
            print("That is not an acceptable value")

#USed to get the step value in one of the calculations
def step_input():
    while True:
        try:
            user_num = int(input("\nPlease enter a number from 1 to 5 for the step value: "))
            if user_num < 1 or user_num > 5:
                raise ValueOutOfRange
            else:
                return user_num

        except ValueOutOfRange:
            print("Sorry that value is not withing the acceptable range")

        except ValueError:
            print("That is not an acceptable value")

#Used to determine the option the user has chosen
def menu_choice():
    while True:
        try:
            menu_input = int(input("\n\nWhat would you like to do?\n0. To quit\n1. To determine even or odd\n2. To determine if it's prime\n3. To determine the prime factors of a number\n4. To determine the sum of all numbers leading up\n5. To sum the digits of the number\n6. To determine if it's a palidrom\n7. To determine the factorial\n8. To determine if it is a distinct number\n"))
            return menu_input
        
        except ValueError:
            print("This is not an acceptable value")

#Main program loop
while True:
    menu_input = menu_choice()
    if menu_input == 0:
        break
    #Odd or even
    elif menu_input == 1:
        user_num = user_input(menu_input)
        if user_num == 0:
            print(f"{user_num} is neither even nor odd")
        elif user_num % 2 == 0:
            print(f"{user_num} is an even number")
        else:
            print(f"{user_num} is not an even number")
    #Prime or not
    elif menu_input == 2:
        prime = True
        user_num = user_input(menu_input)
        if user_num == 0:
            print(f"{user_num} is not a prime number")
        else:
            for i in range(2, user_num):
                if user_num % i == 0:
                    print("Not a prime number")
                    #Print the factors
                    print(f"{i} times {user_num // i} is {user_num}")
                    prime = False
            if prime == True:
                print(f"{user_num} is a prime number")
    #Prime factor the number
    elif menu_input == 3:
        user_num = user_input(menu_input)
        print(f"The prime factors of {user_num} are: ", end="")
        while user_num % 2 == 0:
            print(2, end=", ")
            user_num = user_num / 2
        for i in range(3,int(math.sqrt(user_num)) + 1, 2):
            while user_num % i == 0:
                print(i, end=", ")
                user_num = user_num / i
        if user_num > 2:
            print(f"\n{int(user_num)} can no longer be prime factored")
    #Sum of the numbers leading to the main number
    elif menu_input == 4:
        num_total = 0
        user_num = user_input(menu_input)
        step_value = step_input()
        for i in range(1, user_num + 1, step_value):
            num_total += i
        print(f"The value of summing all values leading up to {user_num} is {num_total}")
    #Sum of the digits
    elif menu_input == 5:
        user_num = user_input(menu_input)
        int_list = list(map(int, str(user_num)))
        print(f"The sum of the digit in the number {user_num} is {sum(int_list)}")
    #Checking for a palindrome
    elif menu_input == 6:
        user_num = user_input(menu_input)
        int_list = list(map(int, str(user_num)))
        reversed_list = list(reversed(int_list))
        if int_list == reversed_list:
            print(f"{user_num} is a palindrome")
        else:
            print(f"{user_num} is not a palindrome")
    #Calculat the facotiral up to 999
    elif menu_input == 7:
        factorial_num = 1
        user_num = user_input(menu_input)
        for i in range(1, user_num + 1):
            factorial_num *= i
        print(f"The value of the factorial of {user_num} is {factorial_num}")
    #Checks for a distinct number
    elif menu_input == 8:
        multiple_num = False
        user_num = user_input(menu_input)
        int_list = list(map(int, str(user_num)))
        for i in range(len(int_list)):
            num_count = int_list.count(int_list[i])
            if num_count > 1:
                multiple_num = True
                print(f"The number {int_list[i]} repeats in the number {user_num}")
        if multiple_num == False:
            print(f"No number repeats in {user_num} so it is a distinct number")
        else:
            print(f"Numbers are repeated in {user_num} therefore it is not distinct")
