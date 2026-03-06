"""Demo of the turtle module that comes with every python distro"""

import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("DarkCyan")

# Use help(obj) to display the docstrings from the module
# print(help(timmy))

my_screen = turtle.Screen()
print(f"Canvas height {my_screen.canvheight}, width {my_screen.canvwidth}")

# movement
timmy.forward(100)

my_screen.exitonclick()
