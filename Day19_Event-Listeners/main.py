from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)

color = ["red","orange","black","green","purple"]
all_turtle = []
y0 = - 80
for turtle_index in range(0, 5) :
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    color_0 = random.choice(color)
    new_turtle.color(color_0)
    color.remove(color_0)
    new_turtle.penup()
    new_turtle.goto(x=-380, y= y0)
    new_turtle.pendown()
    y0 += 40
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Entor a color: ")  

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtle :
        if turtle.xcor() > 380 :
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color :
                print(f"You've won! The {winning_color} turtle is the winner!")
            else :
                print(f"You've lose! The {winning_color} turtle is the winner!")
        else :
            turtle.penup()
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)

screen.exitonclick()