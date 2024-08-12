import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Please guess one random number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, please guess again. Too low")
        elif guess > random_number:
            print("Sorry, please guess again. Too high")

    print(f"yeh congrats you guessed it right!! The number is {random_number}")

guess(10)
