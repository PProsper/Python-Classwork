array = []
Counter = True
while Counter == True:
    Number = int(input("Please enter a number: "))
    array.append(Number)
    end_loop = str(input("Would you like to continue? Y/N:"))
    if end_loop == "N" or end_loop == "n":
        Counter = False
    else:
        Counter = True

#checking for maximum number in list
check = array[0]
for a in array:
    if a < check:
        check = a
print(check)
least = array[0]
for a in array:
    if a > least:
        least = a
print("least")