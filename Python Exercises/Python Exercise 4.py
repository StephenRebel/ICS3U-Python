word_one = input("Please enter a word: ")
word_two = input("Please enter a seconds word: ")

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