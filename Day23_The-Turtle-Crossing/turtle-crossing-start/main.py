import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for the_car in car.cars :
        if player.distance(the_car) < 20 :
            level.game_over()
            game_is_on = False
        if player.check_finish_line() == True :
            player.begin()
            level.plus_score()
            car.level_up()


screen.exitonclick()