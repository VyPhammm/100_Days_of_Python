from turtle import Screen
from paddle import Paddle
from ball import Ball
from crossline import CrossLine
from score import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

crossline = CrossLine()
l_scoreboard = Scoreboard(-40, 250)
r_scoreboard = Scoreboard(40, 250)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350,0)
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > 320) or (ball.distance(l_paddle) <= 50 and ball.xcor() < -320) :
        ball.bounce_x()
    elif ball.xcor() > 400 :
        l_scoreboard.plus_score()
        time.sleep(1)
        ball.goto(0, 0)
        ball.move_speed = 0.1

    elif ball.xcor() < -400 :
        r_scoreboard.plus_score()
        time.sleep(1)
        ball.goto(0, 0) 
        ball.move_speed = 0.1
        
    if l_scoreboard.score == 20 :
        l_scoreboard.game_result(str("Left player"))
        game_is_on = False
    elif r_scoreboard.score == 20 :
        r_scoreboard.game_result(str("Right player"))
        game_is_on = False


screen.exitonclick()