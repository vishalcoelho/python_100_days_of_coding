from turtle import Turtle
import random


class Food(Turtle):

    def __init__(
        self, color: str = "blue", screen_width: int = 600, screen_height: int = 600
    ) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        # Food is 10x10 instead of the default 20x20
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed("fastest")
        self.collision_threshold = 15
        inset = 20
        self.screen_x_lim = (screen_width - 2 * inset) // 2
        self.screen_y_lim = (screen_height - 2 * inset) // 2
        self.refresh()

    def refresh(self) -> None:
        self.goto(
            random.randint(-self.screen_x_lim, self.screen_x_lim),
            random.randint(-self.screen_y_lim, self.screen_y_lim),
        )
