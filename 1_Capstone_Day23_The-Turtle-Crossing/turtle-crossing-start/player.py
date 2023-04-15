from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.color("white")  
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def go_up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)
    
    def check_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else :
            return False
    
    def begin(self):
        self.goto(STARTING_POSITION)


