import random
from words import words
import string


def hangman():
    word = random.choice(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("you used these letters: ", " ".join(used_letters))
        letters_list = [
            letter
            if letter in used_letters
            else "-" for letter in word
        ]
        print("answer: ", " ".join(letters_list))

        user_letters = input("guess the letter: ").upper()

        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

hangman()
