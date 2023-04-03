from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My snake game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.plus_score()
        
    if snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 :
        game_is_on = False
        scoreboard.game_over()
    
    for segment in snake.segments[1:] :
         if snake.head.distance(segment) < 10 :
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
