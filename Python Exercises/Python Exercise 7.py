count = 0
word = ""
print("Please type 'exit' to stop")
while word != "exit":
  while True:
    word = input("Enter a word: ")
    if all(char.isalpha() for char in word) != True:
      print("Input must be a single word")
    else:
      break
  if word != "exit":
    count += 1
print(f"You entered {count} words")

"""
The reason my code does not acknowledge mutiples words entered on one line as multiple words is because it is only counting the number of string inputted not the number of words,to fix this storing the individual words in a list then outputting the length of the list.
"""