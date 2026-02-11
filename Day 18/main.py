from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
for tim in range(20):
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
