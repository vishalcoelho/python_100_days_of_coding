from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forward() -> None:
    """Move the turtle forward by 10 spaces"""
    tim.forward(10)


def move_backward() -> None:
    """Move the turtle backward by 10 spaces"""
    tim.back(10)


def move_clockwise() -> None:
    """Move the turtle clockwise by 5 degrees"""
    tim.right(5)


def move_counter_clockwise() -> None:
    """Move the turtle counter clockwise by 5 degrees"""
    tim.left(5)


def clear_screen() -> None:
    """Clear screen, reset turtle"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def etchASketch() -> None:
    """An Etch-a-Sketch emulator"""

    # Listen for key presses
    screen.listen()

    # register a callback for the "space" key
    # onley is a higher-order function (works with other functions)
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=move_counter_clockwise)
    screen.onkey(key="d", fun=move_clockwise)
    screen.onkey(key="c", fun=clear_screen)

    screen.exitonclick()


if __name__ == "__main__":
    etchASketch()
