
"""
import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%M-%D %H:%M:%S"))

"""
"""
import random

def guess(x):

    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Please guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry guess again, too low.")
        elif guess > random_number:
            print(" Sorry guess again, too high.")
    print(f"yeh congrats, you have guess the number {random_number} correctly!!!")

guess(10)


"""
"""

import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c both are same
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yeh the computer has guessed the number, {guess}, correctly!!!")

computer_guess(10)






import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)???-> ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yeh the computer has guess the number, {guess}, correctly!!!")

computer_guess(10)




print("**************************************************************")


import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Please guess the number between 1 and {x}: "))

        if guess < random_number :
            print("Guess again. Too low.")
        elif guess > random_number:
            print("Guess again. Too high.")
    print(f"Yeh you have guess the number, {random_number}, correctly!!!")

guess(10)






import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could be high as well as both are same

        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)??-> ").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    print(f"Computer has guess the number {guess}, correctly!!!")

computer_guess(10)


"""

print("***Rock, Paper and Scissor***")

import random

def play():
    user = input("Please provide your choice based on 'R' for rock, 'P' for paper and 'S' for scissor: \n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie!!!'

    if is_win(user,computer):
        return "You have Won!"

    return "You have Lost!"

def is_win(player, opponant):
    #r>s, s>p, p>r
    #return true if player wins

    if (player == 'r' and opponant =='s') or (player == 's' and opponant == 'p') or \
            (player == 'p' and opponant == 'r') :
        return True

print(play())








