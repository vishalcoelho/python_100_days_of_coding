from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_INSET = 20

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake - The Game")
# Dont want to see the janky movement of the snake so turn off the tracing
screen.tracer(0)

snake = Snake(color="red")
food = Food()
scoreboard = Scoreboard()

# Create listeners for the arrow keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collisions between the snake and the food
    if snake.head.distance(food) < food.collision_threshold:
        food.refresh()
        snake.grow()
        scoreboard.update()

    # Detect collision with Wall (bounding box)
    bbox_x_lim = SCREEN_WIDTH // 2 - SCREEN_INSET
    bbox_y_lim = SCREEN_HEIGHT // 2 - SCREEN_INSET
    if (
        snake.head.xcor() > bbox_x_lim
        or snake.head.xcor() < -bbox_x_lim
        or snake.head.ycor() > bbox_y_lim
        or snake.head.ycor() < -bbox_y_lim
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if the head collides with any segment (except the head, of course) of the snake, game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
