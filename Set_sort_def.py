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
    #Counter = True
    array.sort()
    print(array)

def maximum(h):
   maxv = h[len(h)-1]
   return maxv

print(maximum(array))

def least(h):
   less = h[0]
   return less

print(least(array))