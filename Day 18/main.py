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

def draw_dots(x, y):
    for _ in range(10):
        for _ in range(10):
            timmy.teleport(x, y)
            timmy.dot(20, random_color())
            x += 40
        x = -200
        y += 40

draw_dots(-200, -200)




screen = Screen()
screen.exitonclick()
