import random
from words import words
import string

def get_valid_word(words):

    word=random.choice(words)

    while '_' in word or ' 'in word:
        word=random.choice(words)

    return word

def hangman():

    word=get_valid_word(words)
    word_letter=set(word) #letter in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #word user guessed

    lives=6

    while len(word_letter)>0 and lives>0:

        print("you have",lives," used these letters: ",' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-'for letter in word]

        print("current word : ", ' '.join(word_list))
        user_letter=input("guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letter:
                 word_letter.remove(user_letter)

            else:
                lives=lives-1
                print("letter is not in the word")

        elif user_letter in used_letters:
            print("you have already used that character try again")

        else:
            print("invalid character, please try again")

    if lives==0:
        print("you died, the word was", word)

    else:
        print("you guessed the word", word)



hangman()
