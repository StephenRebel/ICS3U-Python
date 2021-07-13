num = 0
numlist = []

def manual_sort(numlist):
    newlist = []
    for i in range(len(numlist)):
        minindex = numlist.index(min(numlist))
        newlist.append(numlist.pop(minindex))
        
    return newlist

while num != -1:
    print("Enter -1 to quit:")
    try:
        num = float(input("Enter a number to store: "))
        if num == -1:
            continue
        else:
            numlist.append(num)

    except ValueError:
        print("Not a number...")

print(numlist)
print(manual_sort(numlist))
