from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_x in range(6):
    tim = Turtle(shape= "turtle")
    tim.penup()
    tim.color(colors[turtle_x])
    tim.setposition(x=-230, y= y[turtle_x])
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        distance = random.randint(0, 10)
        turtle.fd(distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")
                



screen.exitonclick()
