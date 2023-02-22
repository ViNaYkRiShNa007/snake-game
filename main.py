from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

game_on = True
screen = Screen()
screen.tracer(0)  # tracer is off
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Score()

screen.listen()  # listens for key strokes

screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")

position = snake.get_position()

# game starts here
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food

    if snake.head.distance(food) < 25:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with the wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset_snake()

    # detect collision of a body part

    for segment in snake.segments[1:]:
        # <- this written because head is the first segment and it cannot detect collision with itself
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()


screen.exitonclick()
