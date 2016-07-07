Counter = int(input ("How many numbers"))
sum = 0
for i in range(Counter):
    number = int(input("What is your number"))
    sum = (sum + number)
Avg = (sum / Counter)

print(Counter)
print (sum)
print(Avg)