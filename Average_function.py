Counter = int(input ("How many numbers"))

def average(a):
    sum = 0
    for i in range(a):
        number = int(input("What is your number"))
        sum = sum + number

    Avg = (sum / a)
    return Avg,sum

print(average(Counter))

print(Counter)
print(sum)