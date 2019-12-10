import random

name = input("What is your name?")
print("Hello " + name + "." )

number = random.randint(10, 20)
guesses = 0
result = False

start = input("Would you like to play a game? [Y/N] ")
if start.lower() == "n":
    print("Goodbye then")
    exit()
if start.lower() == "y":
    print("I'm thinking of a number between 10 & 20")

while not result:
    guess = int(input("Have a guess: "))
    guesses = guesses + 1
    if guess == number:
        result = True
    elif guess < number:
        print("A little Higher")
    elif guess > number:
        print("A little lower")

print("Congrats, you got it right. The number was {}".format(number))
print("it took you {} guesses".format(guesses))
