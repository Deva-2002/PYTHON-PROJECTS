name=input("Type your name: ")

print("welcome ",name," to this adventure")

answer=input("you have reached a dead road, you can only go left and right from here, where you want to go(left/right)? ").lower()

if answer=='left':
    answer=input("you have come to a river , you can walk around it or win through the river, what do you want to do(walk/swim)? ").lower()

    if answer=='swim':
        print("you swimed across and were eaten by an alligator")

    elif answer=='walk':
        print("you walked for many miles and died of exhaustion")

    else:
        print("enter a valid option")

elif answer=='right':
    answer=input("you came to a bridge, it looks wobbly , do you want to cross(cross) or go back(back)? ").lower()

    if answer=='cross':
        answer=input("you crossed the bridge and meet a stranger, you want to talk(yes/no)? ").lower()

        if answer=='yes':
            print("they give you gold and you win")

        elif answer=='no':
            print("you died of social anxiety")

        else:
            print("pls enter a valid option")

    elif answer=='back':
        print("you go back and lost")

    else:
        print("enter a valid option")

else:
    print("not a valid option")

print("thank you for trying ", name)