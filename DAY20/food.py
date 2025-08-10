from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Red")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)#creates a circle
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
