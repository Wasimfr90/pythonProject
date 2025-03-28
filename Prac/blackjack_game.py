# Blackjack game

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score == 0:
        return "Computer has a Blackjack, you Lose!"
    elif u_score > 21:
        return "You went over, you Lose!"
    elif c_score > 21:
        return "Computer went over, you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your first hand : {user_cards}, your score: {user_score}")
        print(f"Computers first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to draw another card, or 'n' to pass:").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"Your Final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's Final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play the game of Blackjack? Type 'y' or 'n':").lower() == 'y':
    print("\n" * 20)
    play_game()








