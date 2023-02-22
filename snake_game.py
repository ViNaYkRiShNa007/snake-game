from turtle import Turtle, Screen
import time

game_on = True

segments = [] # list to store turtle objects
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.tracer(0)  # tracer is off
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

for turtle_index in range(len(starting_positions)):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(starting_positions[turtle_index])
    segments.append(new_segment)

while game_on:
    screen.update()
    time.sleep(1)

    for seg_num in range(len(segments) - 1, 0, -1):
        #gets hold of the last segment and moves it to the last but one's segment's position
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)

# def move_left():
#     for segment in all_turtles:
#         segment.left(90)
#         time.sleep(0.01)
#     screen.update()
#
#
# def move_right():
#     for segment in all_turtles:
#         segment.right(90)
#         time.sleep(0.01)
#     screen.update()
#
#
# screen.onkey(move_left, key="w")
# screen.onkey(move_right, key="s")
screen.exitonclick()
