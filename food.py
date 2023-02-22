import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        # usually turtle is of size of 20 X 20, as we are using this as food we are reducing its dimensions
        self.color("red")

        self.refresh()

    def refresh(self):  # resets the food's position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        pass

    pass
