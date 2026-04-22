from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen_width: int = 600, screen_height: int = 600) -> None:
        super().__init__()
        self.score = -1
        self.penup()
        self.color("white")
        self.hideturtle()
        screen_inset = 30
        self.goto(0, (screen_height - 2 * screen_inset) // 2)
        self.update()

    def update(self) -> None:
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
