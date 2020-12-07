while True:
  try:
    num_ints = int(input("How many integers will you input: "))
    break
  except ValueError:
    print("Input must be an integer")

list_ints = []

for x in range(num_ints):
  while True:
    try:
      get_int = int(input("Please input an integer: "))
      break
    except ValueError:
      print("Input must be an integer")
  list_ints.append(get_int)
list_ints.sort()
print(f"This list is sorted from least to greatest: {list_ints}")
print(f"This is the sum of all integers entered: {sum(list_ints)}")