import string
from art import logo

print(string.ascii_lowercase)
# alphabets = []

print(logo)
print("=======================================================")

def cipher(original_text, shift_to, encode_or_decode):
    cipher_text = ""

    if encode_or_decode == 'decode':
        shift_to *= -1
    else:
        shift_to *= 1

    for latter in original_text:
        if latter not in alphabets:
            cipher_text += latter
        else:
            new_index = alphabets.index(latter) + shift_to
            new_index %= len(alphabets)
            cipher_text += alphabets[new_index]
    print(f"Your {encode_or_decode}d value is : {cipher_text}")


repeat_cipher = True

while repeat_cipher:

    direction = input("Please enter 'encode', if you want to encode, or else enter 'decode':\n").lower()
    text = input("Please enter your text:\n").lower()
    shift = int(input("How much shift you want to make:\n"))

    alphabets = list(string.ascii_lowercase)
    #print(alphabets)
    cipher(original_text=text, shift_to=shift, encode_or_decode=direction)

    repeat_check = input("Do you want to continue, if yes, the type 'yes', or else type 'no':\n").lower()

    if repeat_check == 'no':
        repeat_cipher = False
        print("Goodbye....")
