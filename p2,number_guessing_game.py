# number guessing game

import random

top_of_range=input("enter a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("pls enter a number greater than 0")
        quit()
else:
    print("pls enter a number next time")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses +=1
    user_guess=input("enter your guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please enter a number next time: ")
        continue
    if random_number==user_guess:
        print("you got it correct")
        break
    elif user_guess > random_number:
        print("you are above the number")
    else :
        print("you are below number")

print("you got it in", guesses ,"guesses")