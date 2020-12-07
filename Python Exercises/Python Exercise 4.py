def valid_word(word):
    return all(char.isalpha() for char in word)


while True:
    word_one = input("Please enter a word: ")
    if valid_word(word_one) != True:
        print("Input must be a word")
    else:
        break

while True:
    word_two = input("Please enter a seconds word: ")
    if valid_word(word_two) != True:
        print("Input must be a word")
    else:
        break

"""
In programming and coding something being alphabetically prior to another
is based on the numerical value asociated with the letter, or it's ascii value.
Ascii stands for American Standard Code for Information Interchange. Capital 
letters have a lower value, A = 65, than lower case letters, a = 97. These values
are how we determin alphabetical order in programming.
"""

if word_one > word_two:
    print(f"{word_one} comes alphabetically after {word_two}")
elif word_one < word_two:
    print(f"{word_one} comes alphabetically before {word_two}")
else:
    print(f"{word_one} is alphabetically equal to {word_two}")