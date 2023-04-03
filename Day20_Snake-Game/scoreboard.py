from turtle import Turtle
ALIGNMENT = "center"
FONT= ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Your Score: {self.score}", align= ALIGNMENT, font= FONT)
        self.hideturtle()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Your final Score: {self.score}", align= ALIGNMENT, font= FONT)
    
    def plus_score(self):
        self.clear()
        self.score +=1
        self.write(f"Your Score: {self.score}", align= "center", font=("Arial", 15, "normal"))




