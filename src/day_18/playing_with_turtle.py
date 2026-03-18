from turtle import Turtle, Screen, colormode
import random
from typing import Tuple

tim = Turtle()
colormode(255)

tim.shape("turtle")
tim.color("red")

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# tim.reset()
# tim.color("blue")
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

tim.reset()

# Draw polygons
# tim.pendown()
# tim.shape("turtle")
# color = [
#     "red",
#     "green",
#     "blue",
#     "chartreuse3",
#     "DarkOrchid3",
#     "coral1",
#     "DeepPink",
#     "azure4",
#     "burlywood4",
# ]
# for n_sides in range(3, 11):
#     internal_angle = 360 / n_sides
#     tim.color(color[n_sides - 2])
#     for _ in range(n_sides):
#         tim.forward(100)
#         tim.right(internal_angle)


def random_color() -> Tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Random walk
# tim.reset()
# tim.speed("fastest")
# tim.pensize(10)
# angle = [0, 90, 270, 180]
# color = [
#     "red",
#     "green",
#     "blue",
#     "chartreuse3",
#     "DarkOrchid3",
#     "coral1",
#     "DeepPink",
#     "azure4",
#     "burlywood4",
# ]
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(angle))
#     tim.pencolor(random_color())

# Spirograph
tim.reset()
tim.speed("fastest")
outer_radius = 100
angular_step = 5
for _ in range(int(360 / angular_step)):
    tim.circle(outer_radius, extent=angular_step)
    tim.pencolor(random_color())
    tim.circle(outer_radius / 2)

screen = Screen()
screen.exitonclick()
