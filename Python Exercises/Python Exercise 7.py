count = 0
word = ""
print("Please type 'exit' to stop")
while word != "exit":
  word = input("Enter a word: ")
  if word != "exit":
    count += 1
print(f"You entered {count} words")

"""
The reason my code does not acknowledge mutiples words entered on one line as multiple words is because it is only counting the number of string inputted not the number of words,to fix this storing the individual words in a list then outputting the length of the list.
"""