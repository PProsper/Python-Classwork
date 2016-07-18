import random
Guess = 0
print('Please enter a number: ')
Number = random.randint(1,10)
guesses = int(input())
Guess = Guess + 1

while Guess < 6:
        if guesses < Number:
            print("warm")
        if guesses > Number:
            print("cold")
        if guesses == Number:
            Guess = int(guesses)
            print("hot! You guessed right!")
            break
        if guesses != Number:
            Number = int(Number)
            print('No. The number is  ' + str(Number))
            break



