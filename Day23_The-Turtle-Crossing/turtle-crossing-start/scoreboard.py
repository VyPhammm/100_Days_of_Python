from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align= "left", font= FONT)
        self.hideturtle() 
    
    def plus_score(self):
        self.clear()
        self.score +=1
        self.write(f"Level: {self.score}", align= "left", font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= FONT)