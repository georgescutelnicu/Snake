from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


is_game_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("The Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.snake_head.distance(food) < 18:
        scoreboard.increase_score()
        scoreboard.refresh_score()
        food.refresh_food()
        snake.snake_extend()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    for segment in snake.segments[3:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()




screen.exitonclick()