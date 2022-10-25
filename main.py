import random
from turtle import Screen
import time
from food import Food
from scoreboards import ScoreBoard
from snake import Snake

snake = Snake()
food = Food()
screen = Screen()

screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        scoreboard.increase_score()
        snake.increase_snake()
    if snake.segments[0].pos()[0] < -280 or snake.segments[0].pos()[0] > 280 or snake.segments[0].pos()[1] < -280 or snake.segments[0].pos()[1] > 280 or snake.hit_body():
        snake.reset()
        scoreboard.reset()





screen.exitonclick()
