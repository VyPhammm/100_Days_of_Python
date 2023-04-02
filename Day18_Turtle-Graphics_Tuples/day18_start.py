from turtle import Turtle, Screen, colormode, pos
import random


t = Turtle()

color = ["#6495ED","#00FF00", "#B8860B", "#8B008B", "#FFF5EE", "#FF7F50", "#FF4500", "#F08080", "#FAEBD7", "#9400D3", "#F0E68C", "#00FF7F", "#008080", "#87CEFA", "#696969", "#778899", "#000000"]
angle = [0,90,180,270]

# for _ in range(4,11) :
#     draw(_)

# for i in range(15) :
#     t.forward(5)
#     t.penup()
#     t.forward(5)
#     t.pendown()
t.pensize(20)
t.speed(15)
colormode(255)

def draw(number) :
    angle = int(360/number)
    for _ in range(number) :
        t.left(angle)
        t.forward(100)

def random_color() :
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


def random_move() :
    move = True
    while move :
        t.pencolor(random_color())
        angle_random = random.choice(angle)
        t.setheading(angle_random)
        t.forward(20)

def draw_multi_circle(size_of_gap) :
    for _ in range(int(360 /size_of_gap)) :
        t.pencolor(random_color())
        t.left(0 + size_of_gap)
        t.circle(10)

def draw_one_row(n) :
    for _ in range(n) :
        draw_multi_circle(360)
        t.penup()
        t.forward(50)
        t.pendown()

def picture(n):
        for _ in range(n) :
            draw_one_row(10)
            t.left(90)
            t.penup()
            t.forward(50)
            t.left(90)
            t.forward(300)
            t.left(180)
            t.pendown()



picture(10)


screen = Screen()
screen.exitonclick()
