from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")

colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
def draw_shape(num_sides):
    angle = 360/num_sides
    for x in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for sides in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(sides)



screen = Screen()
screen.exitonclick()
