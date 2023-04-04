from turtle import Turtle
import random

K = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")  
        self.shapesize(1, 1)
        self.setposition(0, 0)

    def move(self):
        new_x = self.xcor() + K
        new_y = self.ycor() + K
        self.goto(new_x, new_y)