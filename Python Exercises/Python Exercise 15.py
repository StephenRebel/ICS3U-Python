class ValueOutOfRange(Exception):
  pass

while True:
  try:
    test_score = int(input("Please enter a test score between 0 and 100: "))
    if test_score >= 0 and test_score <= 100:
      print(f"The test score was {test_score}")
      break
    else:
      raise ValueOutOfRange

  except ValueOutOfRange:
    print("This test score is not within the acceptable range of 0 and 100")

  except ValueError:
    print("This value is not an intager")