import random

computer_wins=0
user_wins=0

options=['rock','paper','scissor']
while True:
    user_input=input("enter rock/paper/scissor or q if you want to quit: ").lower()

    if user_input=='q':
        break

    if user_input not in options:
        print("pls enter a valid option")
        continue

    random_number=random.randint(0,2)
    computer_input=options[random_number]
    print("computer picked"+computer_input+".")

    if user_input == 'rock' and computer_input== 'scissor':
        print("you win! ")
        user_wins+=1
    elif user_input == 'paper' and computer_input== 'rock':
        print("you win! ")
        user_wins+=1
    elif user_input == 'scissor' and computer_input== 'paper':
        print("you win! ")
        user_wins+=1
    else:
        print("you lost")
        computer_wins+=1

print("you won ",user_wins," times")
print("computer won ",computer_wins," times")

