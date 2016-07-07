array = []
Counter = True
while Counter == True:
    Number = int(input("Please enter a number: "))
    array.append(Number)
    end_loop = str(input("Would you like to continue? Y/N:"))
    if end_loop == "n" or end_loop == "N":
        Counter = False
    else:
        Counter = True
    print(array)
#checking for maximum number in list

check = array[0]
for a in array:
    # other way of writing : in range (0,check) """"if done this way, a is not an
    #  index within array but a co
    if a > check:
        check = a
        print(check)

check = array[0]
for a in array:
    # other way of writing : in range (0,check)
    if a < check:
        check = a
        print(check)
