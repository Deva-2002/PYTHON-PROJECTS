import random

def roll():
    max_value=6
    min_value=1
    roll=random.randint(min_value,max_value)
    return roll

while True:
    players=input("Enter the no of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("enter a valid number between 1 and 4")
    else:
        print("please enter a numeric value")

max_score=50
player_score=[0 for _ in range(players)]

while max(player_score)<max_score:

    for player_idx in range(players):
        print("\nPlayer number",player_idx +1,"turn has just started!")
        print("your total score is :",player_score[player_idx],"/n")
        current_score=0

        while True:

            should_roll=input("would you like to roll (y)? ")
            if should_roll.lower()!= "y":
                break
            value=roll()

            if value == 1:
                print("You rolled a 1! Turn done !")
                current_score=0
                break
            else:
                current_score +=value
                print("You rolled a: ",value)

            print("Your score is: ",current_score)


        player_score[player_idx]+=current_score
        print("Your total score is :",player_score[player_idx])

max_score=max(player_score)
winning_index=player_score.index(max_score)
print("players number",winning_index+1,"is the winner with a score of :",max_score)
