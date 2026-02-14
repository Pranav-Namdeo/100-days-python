from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(5)
timmy.speed("fastest")

colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for x in range(1000):
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(20)





screen = Screen()
screen.exitonclick()
