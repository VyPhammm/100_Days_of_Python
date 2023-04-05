from turtle import Turtle
ALIGNMENT = "center"
FONT= ("Arial", 25, "normal")

class Scoreboard(Turtle):

    def __init__(self, x_pos, y_pos) :
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x_pos, y_pos)
        self.write(f"{self.score}", align= ALIGNMENT, font= FONT)
        self.hideturtle()
        
    
    def plus_score(self):
        self.clear()
        self.score +=1
        self.write(f"{self.score}", align= ALIGNMENT, font= FONT)

    def game_result(self, player):
        self.goto(0, 0)
        self.write(f"{player} is the winner", align= ALIGNMENT, font= FONT)

    