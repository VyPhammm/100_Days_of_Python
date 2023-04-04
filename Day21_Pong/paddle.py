from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.create_paddle(x_pos, y_pos)

    def create_paddle(self, x_pos, y_pos):
        self.shape("square")
        self.penup()
        self.color("white")  
        self.shapesize(5, 1)
        self.setposition(x_pos , y_pos)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)