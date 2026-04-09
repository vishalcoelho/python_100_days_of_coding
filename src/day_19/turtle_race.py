from turtle import Turtle, Screen
import sys
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

if user_bet in colors:
    is_race_on = True
else:
    print("Invalid bet...Exiting")
    sys.exit()


turtle_list = []
for i, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=99 - 33 * i)
    turtle_list.append(new_turtle)

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(0, 10))

        # turtle body is 40x40, so finish line is 230
        #       230  250
        #         v  v
        #         |  |
        #      +-----+
        #      |20|20|
        #      +-----+
        #         |  |
        if turtle.xcor() > 230:
            # One of the turtles finished the race, stop
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You win! you predicted {turtle.pencolor()} would win")
            else:
                print(f"You lost! you bet on {user_bet} but {turtle.pencolor()} won")


screen.exitonclick()
