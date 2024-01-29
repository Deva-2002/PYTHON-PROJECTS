import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS=['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():

    racers=0

    while True:

        racers=input("enter the number of racers(2-10): ")

        if racers.isdigit():

            racers=int(racers)
        else:
            print("input is not numeric try again!")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("number is not in range betwwn 2 and 10, try again!")


def race(colors):

    turtles=create_turtles(colors)

    while True:

        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(turtle)]




def create_turtles(colors):

    turtles=[]
    spacingX=WIDTH//(len(colors)+1)

    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacingX,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():

    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("TURTLE RACING!")

racers=get_number_of_racers()

init_turtle()

random.shuffle(COLORS)
colors=COLORS[:racers]

winner=race(colors)
print("winner is the turtle with color: ",winner)
time.sleep(5)