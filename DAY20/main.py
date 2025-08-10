#The Snake Game by Parmeet Singh
from turtle import Screen
from Scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.left, key="a")
screen.onkey(snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() < -290 or
        snake.head.xcor() > 290 or
        snake.head.ycor() < -290 or
        snake.head.ycor() > 290
    ):
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

# Show game over message no matter how the game ended
scoreboard.game_over()

screen.exitonclick()
