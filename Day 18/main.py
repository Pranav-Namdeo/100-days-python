from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(2)
timmy.speed("fastest")

colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for x in range(0, 360, 10):
    timmy.color(random_color())
    timmy.setheading(x)
    timmy.circle(100)



screen = Screen()
screen.exitonclick()
