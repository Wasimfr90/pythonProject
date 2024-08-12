#rock paper and scissors

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'

    #r>s, s>p, p>r
    if is_win(user,computer):
        return 'You won!'

    return 'You lost!'
def is_win(player, opponant):
    #return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponant == 's') or (player == 's' and opponant == 'p')\
            or (player == 'p' and opponant =='r'):
        return True

print(play())
