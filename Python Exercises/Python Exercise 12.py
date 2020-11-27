def converter_cel_to_far(temp):
  return round(float(((9 * temp) / 5) + 32),1)

print(converter_cel_to_far(0))
print(converter_cel_to_far(28))
print(converter_cel_to_far(34))
print(converter_cel_to_far(-15))