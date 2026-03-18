from pprint import pprint
from pathlib import Path
import random
import turtle
import colorgram
from typing import Tuple


def draw_dot(turtle: turtle.Turtle, heading, color: Tuple[int, int, int]) -> None:
    # Note: turtle has a dot method that can be used instead of this
    turtle.pendown()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    if heading == 0:  # east
        turtle.circle(10)
    else:
        turtle.circle(-10)
    turtle.end_fill()
    turtle.penup()


image_path = Path("src/day_18/damien_hirst_spot_painting.jpg")
# Extract all colors from the painting
colors = colorgram.extract(image_path.absolute(), 50)
pprint(colors)
# Note: background colors (shades of white) will be part of this list!
list_of_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()

# Start from the lower left quadrant
tim.teleport(-60 * 5, -60 * 5)

# move in a grid pattern and draw dots
scan_dir = 0  # east moving first
for _ in range(10):
    draw_dot(tim, scan_dir, random.choice(list_of_colors))
    for _ in range(10):
        tim.forward(60)
        draw_dot(tim, scan_dir, random.choice(list_of_colors))
    tim.setheading(90)
    tim.forward(60)
    scan_dir += 180
    scan_dir %= 360
    tim.setheading(scan_dir)

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
