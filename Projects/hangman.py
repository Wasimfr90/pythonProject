import random
import string

from words import words

def get_valid_words(words):
    word = random.choice(words) #randomly choose from the list

    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) #letters in the word
    alphabet  = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting user input
    user_letter = input("Guess a letter: ").upper()

user_input = input("type something: ")
print(user_input)

