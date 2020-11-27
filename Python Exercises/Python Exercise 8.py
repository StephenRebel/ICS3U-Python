start = int(input("Enter a starting value: "))
end = int(input("Enter a ending value: "))
step = int(input("What is the increment: "))

num_list = list(range(start, end, step))

print("{:<10}{:>12}".format("List value","Square"))
for x in range(len(num_list)):
  print("{:>6}{:>15}".format(num_list[x],(num_list[x])**2))