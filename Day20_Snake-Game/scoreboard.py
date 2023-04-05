from turtle import Turtle
ALIGNMENT = "center"
FONT= ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self) :
        super().__init__()
        self.color("white")
        self.score = 0
        with open("Day20_Snake-Game\data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} High score: {self.high_score}", align= "center", font=("Arial", 15, "normal"))

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day20_Snake-Game\data.txt", mode= "w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def plus_score(self):
        self.score +=1
        self.update_scoreboard()




